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