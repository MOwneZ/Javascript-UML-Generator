class Pool {
  constructor (newName) {
    this.name = newName
    this.allMyTeams = []
    this.allMyMatches = []
  }
  addTeam(aTeam){
    if (! this.allMyTeams.includes(aTeam)) {
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
  getTeams() {
    this.sortTeams()
    let result = 'Pool ' + this.name + View.NEWLINE()
      for (let aTeam of this.allMyTeams) {
        result += View.TAB() + aTeam + View.NEWLINE()
      }
    return result
  }
  
  toString () {
    return 'Pool ' + this.name
  }

  addMatch(aMatch){
    this.allMyMatches.push(aMatch)
  }
  
  sortTeamsByRank () {
    this.allMyTeams.sort((a, b) => {
      if (a.matchesWon > b.matchesWon) {
        return -1
      }
      if (a.matchesWon < b.matchesWon) {
        return 1
      } // a must be equal to b
      return 0
    })
  }

  findMatch(teamA, teamB) {
      return this.allMyMatches.find(aMatch => ((aMatch.myTeamA === teamA && aMatch.myTeamB === teamB) || (aMatch.myTeamB === teamA && aMatch.myTeamA === teamB)))
  }
  
  getResults () {
    this.sortTeamsByRank()
    let result = ''
    let topLine = View.SPACES(6)
    for (let aTeamForTopLine of this.allMyTeams){
        let topName = aTeamForTopLine.shortName
        topLine += View.centre(topName, 7)
        let sideName = aTeamForTopLine.shortName
        result += sideName + View.SPACES(2)
        for (let aTeamForSide of this.allMyTeams){
          if (topName === aTeamForSide.shortName) {
            result += View.centre('XXXXX', 7)
          }
          else {
            
            let theMatch = this.findMatch(aTeamForTopLine, aTeamForSide)
            let leftScore = theMatch.findScore(aTeamForTopLine.name)
            let rightScore = theMatch.findScore(aTeamForSide.name)
            let score = `${leftScore}-${rightScore}`
            
            //let score = '99-00'
            result += View.centre(score, 7)
          }

        }
        result += aTeamForTopLine.getResults() + View.NEWLINE()
    }
    topLine += View.padRight('Played')
    topLine += View.padRight('Won')
    topLine += View.padRight('Lost')
    topLine += View.padRight('Draw')
    topLine += View.padRight('For')
    topLine += View.padRight('Against')
    result = topLine + View.NEWLINE() + result + View.NEWLINE()
    return result
  }
}