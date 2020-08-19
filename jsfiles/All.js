class Match {
  constructor ( when, thePool, teamA, teamB ) {
    this.when = when
    this.myPool = thePool
    this.myTeamA = teamA
    this.myTeamB = teamB
    this.scoreA = null
    this.scoreB = null
  }
  hasTeam(targetName) {
    return this.myTeamA.name === targetName || this.myTeamB.name === targetName
  }
  toString() {
    //return `${this.when.toDateString()} ${this.when.toLocaleTimeString()} ${this.myPool} ${this.myTeamA} vs ${this.myTeamB} `
    return `${this.myPool} ${this.myTeamA} vs ${this.myTeamB} ${this.scoreA} - ${this.scoreB}`
    
  }
  
  addResult (newScoreA, newScoreB) {
      this.scoreA = newScoreA
      this.scoreB = newScoreB
      
      this.myTeamA.incPlayed()
      this.myTeamA.incScoreFor(newScoreA)
      this.myTeamA.incScoreAgainst(newScoreB)
    
      this.myTeamB.incPlayed()
      this.myTeamB.incScoreFor(newScoreB)
      this.myTeamB.incScoreAgainst(newScoreA)
    
      if (newScoreA > newScoreB ) {
          this.myTeamA.incWin()
          this.myTeamB.incLoss()
      }
      if (newScoreA < newScoreB ) {
          this.myTeamB.incWin()
          this.myTeamA.incLoss()
      }
  }
  
  findScore(targetTeamName){
    let score = this.scoreA
    if (this.myTeamA.name !== targetTeamName){
      score = this.scoreB
    }
    return score
  }
}

class Sport {
  constructor (newName, newVenue) {
    this.name = newName
    this.venue = newVenue
    this.allMyPools = []
    this.allMyTeams = []
    this.allMyMatches = []
  }
  toString() {
      return `${this.name} at ${this.venue}`
  }
  findTeam (targetName) {
    return this.allMyTeams.find(aTeam => aTeam.name === targetName)
  }
  addTeam(newName){
    let aTeam = this.findTeam(newName) 
    if (! aTeam) {
      aTeam = new Team(newName)
      this.allMyTeams.push(aTeam)
    }
    return aTeam
  }
  sortTeams () {
    this.allMyTeams.sort((a, b) => {
      if (a.name < b.name) {
        return -1
      }
      if (a.name > b.name) {
        return 1
      } // a must be equal to b
      return 0
    })
  } 

  findPool (targetName) {
     return this.allMyPools.find(aPool => aPool.name === targetName)
  }
  sortPools () {
    this.allMyPools.sort((a, b) => {
      if (a.name < b.name) {
        return -1
      }
      if (a.name > b.name) {
        return 1
      } // a must be equal to b
      return 0
    })
  }
  addPool (newName) {
    let name = newName.trim()
    let aPool = this.findPool(name) 
    if (! aPool) {
      aPool = new Pool(name)
      this.allMyPools.push(aPool)
    }
    return aPool
  }
  addMatch(newYear, newMonth, newDay, newHour, newMinute, newPoolName, newTeamNameA, newTeamNameB){
    let when = new Date(newYear, newMonth, newDay, newHour, newMinute)
    let thePool = this.addPool(newPoolName)
    let teamA = this.addTeam(newTeamNameA)
    let teamB = this.addTeam(newTeamNameB)
    thePool.addTeam(teamA)
    thePool.addTeam(teamB)
    let newMatch = new Match(when, thePool, teamA, teamB)
    this.allMyMatches.push(newMatch)
    }
  sortMatches() {
    this.allMyMatches.sort((a, b) => {
      if (a.when < b.when) {
        return -1
      }
      if (a.when > b.when) {
        return 1
      } // same time - now sort by pool
      return 0
    })
  }
  getTeams() {
    this.sortTeams()
    let result = '*' + this.name + View.NEWLINE()
    for (let aTeam of this.allMyTeams) {
      result += aTeam + View.NEWLINE()
    }
    result += View.NEWLINE()
    return result
  }
  getPools () {
    this.sortPools()
    let result = '*' + this.name + View.NEWLINE()
    for (let aPool of this.allMyPools) {
      result += aPool.getTeams() + View.NEWLINE()
    }
    return result
  }
  
  
    sortMatchesByPool ()  {
    this.allMyMatches.sort((a,b) => {
      if (a.myPool.name < b.myPool.name) {
        return -1
      }
      if (a.myPool.name > b.myPool.name) {
        return 1
      }
       else{
         return 0
       }
  })
    
  }
  
  getMatchResults () {
    this.sortMatchesByPool()
    let result = '*' + this.name + View.NEWLINE()
    for (let aMatch of this.allMyMatches) {
      result += aMatch + View.NEWLINE()
    }
    return result
  }
  
  
  getNZMatches () {
    this.sortMatchesByPool()
    let result = '*' + this.name + View.NEWLINE()
    for (let aMatch of this.allMyMatches) {
      if (aMatch.hasTeam('New Zealand')) {
        result += aMatch + View.NEWLINE()
      }
    }
    return result
  }
  //--------------------------------------------------------------------------
  findMatch(winner, looser) {
   return this.allMyMatches.find(aMatch => ((aMatch.myTeamA === winner && aMatch.myTeamB === looser) || (aMatch.myTeamB === winner && aMatch.myTeamA === looser)))
  }
  
  addPoolResult (winnerName, looserName, newWinnwerScore, newLooserScore) {
    let winner = this.findTeam(winnerName)
    let looser = this.findTeam(looserName)
    let theMatch = this.findMatch(winner, looser)
    let scoreA = newWinnwerScore
    let scoreB = newLooserScore
    if (theMatch.myTeamA.name !== winner.name){
      scoreA = newLooserScore
      scoreB = newWinnwerScore
    }
    theMatch.addResult(scoreA, scoreB)
  }

  addShortName (fullTeamName, shortTeamName){
    let theTeam = this.findTeam(fullTeamName)
    theTeam.shortName = shortTeamName
  }
  
  getResults () {
    let result = `Results for ${this.name}` + View.NEWLINE()
    this.sortPools()
    for (let aMatch of this.allMyMatches) {
      let thePool = aMatch.myPool
      thePool.addMatch(aMatch)
    }
    
    for (let aPool of this.allMyPools) {
      result += aPool + View.NEWLINE()
      result += aPool.getResults()
    }
    return result
  }
  
    sortTeams () {
    this.allMyTeams.sort((a, b) => {
      if (a.name < b.name) {
        return -1
      }
      if (a.name > b.name) {
        return 1
      } // a must be equal to b
      return 0
    })
  } 
  
  
    getTeamResults() {
    this.sortTeams()
    let result = '*' + this.name + View.NEWLINE()
    for (let aTeam of this.allMyTeams) {
      result += View.padRight(aTeam, 20) + aTeam.getResults() + View.NEWLINE()
    }
    result += View.NEWLINE()
    return result
  }
}

class Team {
  constructor (newName) {
    this.name = newName
    this.shortName = ''
    this.matchesPlayed = 0
    this.matchesWon = 0
    this.matchesLost = 0
    this.matchesDrawn = 0
    this.scoreFor = 0
    this.scoreAgainst = 0
    this.poolRank = 0
  }
  incWin() {
    this.matchesWon += 1 
  }
  incLoss() {
    this.matchesLost += 1 
  }
  incPlayed() {
    this.matchesPlayed += 1
  }
  incScoreFor(newScoreFor) {
    this.scoreFor += newScoreFor
  }
  incScoreAgainst(newScoreAgainst) {
    this.scoreAgainst += newScoreAgainst 
  }
  toString() {
    return this.name
  }
  getResults () {
    let result = View.SPACES(4)
    result += View.padRight(this.matchesPlayed)
    result += View.padRight(this.matchesWon)
    result += View.padRight(this.matchesLost)
    result += View.padRight(this.matchesDrawn)
    result += View.padRight(this.scoreFor)
    result += View.padRight(this.scoreAgainst)
    return result
  }
}

class Tournament {
  constructor (newName) {
    this.name = newName
    this.allMySports = []
  }
  toString() {
    return this.name
  }
  addSport(newName, newVenue) {
    let newSport = new Sport(newName, newVenue)
    this.allMySports.push(newSport)
    return newSport
  }
  
  getSports() {
    let result = ''
    for (let aSport of this.allMySports) {
      result += aSport + View.NEWLINE()
    }
    return result
  }
  getTeams() {
    let result = ''
    for (let aSport of this.allMySports) {
      result += aSport.getTeams() + View.NEWLINE()
    }
    return result
  }
  getPools() {
    let result = ''
    for (let aSport of this.allMySports) {
      result += aSport.getPools() + View.NEWLINE()
    }
    return result
  }

  getMatches() {
    let result = ''
    for (let aSport of this.allMySports) {
      result += aSport.getMatches() + View.NEWLINE()
    }
    return result
  }
  getNZMatches() {
    let result = ''
    for (let aSport of this.allMySports) {
      result += aSport.getNZMatches() + View.NEWLINE()
    }
    return result
  }
  getParticipation () {
    let result = ''
    
    let netballSet = new  Set()
    for (let aTeam of this.allMySports[0].allMyTeams) {
      netballSet.add(aTeam.name)
    }
    let mens7sSet = new  Set()
    for (let aTeam of this.allMySports[1].allMyTeams) {
      mens7sSet.add(aTeam.name)
    }
    let womens7sSet = new  Set()
    for (let aTeam of this.allMySports[2].allMyTeams) {
      womens7sSet.add(aTeam.name)
    }
    let all3Set = netballSet.intersection(mens7sSet)
    all3Set = all3Set.intersection(womens7sSet)
  }
  
  getResults () {
    let result = ''
    for (let aSport of this.allMySports) {
      result += aSport.getResults() + View.NEWLINE()
    }
    return result
  }
  
    getMatchResults() {
    let result = ''
    for (let aSport of this.allMySports) {
      result += aSport.getMatchResults() + View.NEWLINE()
    }
    return result
  }
  
    getTeamResults() {
    let result = ''
    for (let aSport of this.allMySports) {
      result += aSport.getTeamResults() + View.NEWLINE()
    }
    return result
  }
  
  getAll() {
    let result = 'Programming Assignment 2' + View.NEWLINE()
    result += this + View.NEWLINE()
    //result += 'TEAMS' + View.NEWLINE() +  View.NEWLINE() + this.getSports() + View.NEWLINE()
    //result += 'TEAMS' + View.NEWLINE() +  View.NEWLINE() + this.getTeams() + View.NEWLINE()
    //result += 'POOLS' + View.NEWLINE() +  View.NEWLINE() + this.getPools() + View.NEWLINE()
    result += 'MATCH RESULTS' + View.NEWLINE() +  View.NEWLINE() + this.getMatchResults() + View.NEWLINE()
    result += 'TEAM RESULTS' + View.NEWLINE() +  View.NEWLINE() + this.getTeamResults() + View.NEWLINE()
    //result += 'NZ MATCHES' + View.NEWLINE() +  View.NEWLINE() + this.getNZMatches() + View.NEWLINE()
    //result += 'PARTICIPATION ANALYSIS' + View.NEWLINE() +  View.NEWLINE() + this.getParticipation() + View.NEWLINE()
    result += 'MATCHES RESULTS' + View.NEWLINE() +  View.NEWLINE() + this.getResults() + View.NEWLINE()
    return result
  }
  
  findSport (targetName) {
    return this.allMySports.find(aSport => aSport.name === targetName)
  }
}