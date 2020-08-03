class Controller {
  static setup () {
    const APRIL = 3 // JAN = 0!  
    let the2018Games = new Tournament('Gold Coast 2018 Commonwealth Games')
    let aSport = the2018Games.addSport('Netball', 'Gold Coast Convention and Exhibition Centre')
    
    // -----------------------------------------------------------------------------
    aSport.addMatch(2018, APRIL,  5, 13,  0, 'A', 'Jamaica', 'Fiji')
    aSport.addMatch(2018, APRIL,  5, 15,  0, 'B', 'England', 'Scotland')
    aSport.addMatch(2018, APRIL,  5, 18, 30, 'B', 'New Zealand', 'Uganda') 
    aSport.addMatch(2018, APRIL,  5, 20, 30, 'A', 'Australia', 'Northern Ireland')

    aSport.addMatch(2018, APRIL,  6, 13,  0, 'B', 'Wales', 'New Zealand')
    aSport.addMatch(2018, APRIL,  6, 15,  0, 'A', 'South Africa', 'Jamaica')
    aSport.addMatch(2018, APRIL,  6, 18, 30, 'B', 'Malawi', 'England')
    aSport.addMatch(2018, APRIL,  6, 20, 30, 'A', 'Barbados', 'Australia')

    aSport.addMatch(2018, APRIL,  7, 13,  0, 'B', 'Uganda', 'Malawi')
    aSport.addMatch(2018, APRIL,  7, 15,  0, 'A', 'Northern Ireland', 'South Africa')
    aSport.addMatch(2018, APRIL,  7, 18, 30, 'B', 'Scotland', 'Wales')
    aSport.addMatch(2018, APRIL,  7, 20, 30, 'A', 'Fiji', 'Barbados')

    aSport.addMatch(2018, APRIL,  8, 13,  0, 'A', 'Jamaica', 'Northern Ireland')
    aSport.addMatch(2018, APRIL,  8, 15,  0, 'B', 'England', 'Uganda')
    aSport.addMatch(2018, APRIL,  8, 18, 30, 'B', 'Malawi', 'New Zealand')
    aSport.addMatch(2018, APRIL,  8, 20, 30, 'A', 'Australia', 'South Africa')

    aSport.addMatch(2018, APRIL,  9, 13,  0, 'B', 'England', 'Wales')
    aSport.addMatch(2018, APRIL,  9, 15,  0, 'A', 'Fiji', 'Australia')
    aSport.addMatch(2018, APRIL,  9, 18, 30, 'A', 'Jamaica', 'Barbados')
    aSport.addMatch(2018, APRIL,  9, 20, 30, 'B', 'New Zealand', 'Scotland')

    aSport.addMatch(2018, APRIL, 10, 13,  0, 'A', 'Barbados', 'Northern Ireland')
    aSport.addMatch(2018, APRIL, 10, 15,  0, 'B', 'Scotland', 'Malawi')
    aSport.addMatch(2018, APRIL, 10, 18, 30, 'A', 'South Africa', 'Fiji')
    aSport.addMatch(2018, APRIL, 10, 20, 30, 'B', 'Wales', 'Uganda')

    aSport.addMatch(2018, APRIL, 11,  9,  0, 'B', 'New Zealand', 'England')
    aSport.addMatch(2018, APRIL, 11, 11,  0, 'A', 'South Africa', 'Barbados')
    aSport.addMatch(2018, APRIL, 11, 14,  0, 'A', 'Northern Ireland', 'Fiji')
    aSport.addMatch(2018, APRIL, 11, 16,  0, 'B', 'Uganda', 'Scotland')
    aSport.addMatch(2018, APRIL, 11, 19,  0, 'B', 'Malawi', 'Wales')
    aSport.addMatch(2018, APRIL, 11, 21,  0, 'A', 'Australia', 'Jamaica')

    
    // -----------------------------------------------------------------------------
    aSport = the2018Games.addSport('Men\'s Rugby Sevens', 'Robina Stadium')

    aSport.addMatch(2018, APRIL, 14,  9, 30, 'B', 'Australia', 'Samoa')
    aSport.addMatch(2018, APRIL, 14,  9, 30, 'B', 'England', 'Jamaica')
    aSport.addMatch(2018, APRIL, 14, 10, 30, 'C', 'Canada', 'Kenya')
    aSport.addMatch(2018, APRIL, 14, 10, 30, 'C', 'New Zealand', 'Zambia')
    aSport.addMatch(2018, APRIL, 14, 11, 30, 'D', 'Wales', 'Uganda')
    aSport.addMatch(2018, APRIL, 14, 11, 30, 'D', 'Fiji', 'Sri Lanka')
    aSport.addMatch(2018, APRIL, 14, 12, 30, 'A', 'Scotland', 'Papua New Guinea')
    aSport.addMatch(2018, APRIL, 14, 12, 20,'A', 'South Africa', 'Malaysia')

    aSport.addMatch(2018, APRIL, 14, 14, 30, 'B', 'Australia', 'Jamaica')
    aSport.addMatch(2018, APRIL, 14, 14, 30, 'B', 'England', 'Samoa')
    aSport.addMatch(2018, APRIL, 14, 15, 30, 'C', 'Canada', 'Zambia')
    aSport.addMatch(2018, APRIL, 14, 15, 30, 'C', 'New Zealand', 'Kenya')

    aSport.addMatch(2018, APRIL, 14, 17, 30, 'D', 'Wales', 'Sri Lanka')
    aSport.addMatch(2018, APRIL, 14, 17, 30, 'D', 'Fiji', 'Uganda')
    aSport.addMatch(2018, APRIL, 14, 18,  0, 'A', 'Scotland', 'Malaysia')
    aSport.addMatch(2018, APRIL, 14, 18,  0, 'A', 'South Africa', 'Papua New Guinea')


    aSport.addMatch(2018, APRIL, 14, 19,  0, 'B', 'Samoa', 'Jamaica')
    aSport.addMatch(2018, APRIL, 14, 19,  0, 'B', 'England', 'Australia')
    aSport.addMatch(2018, APRIL, 14, 19, 30, 'C', 'Kenya', 'Zambia')
    aSport.addMatch(2018, APRIL, 14, 19, 30, 'C', 'New Zealand', 'Canada')
    aSport.addMatch(2018, APRIL, 14, 20,  0, 'D', 'Uganda', 'Sri Lanka')
    aSport.addMatch(2018, APRIL, 14, 20,  0, 'D', 'Fiji', 'Wales')
    aSport.addMatch(2018, APRIL, 14, 20, 30, 'A', 'Papua New Guinea', 'Malaysia')
    aSport.addMatch(2018, APRIL, 14, 20, 30, 'A', 'South Africa', 'Scotland')

    // -----------------------------------------------------------------------------
    aSport = the2018Games.addSport('Women\'s Rugby Sevens', 'Robina Stadium')
    aSport.addMatch(2018, APRIL, 13, 16, 30, 'A', 'Canada', 'South Africa')
    aSport.addMatch(2018, APRIL, 13, 16, 30, 'A', 'New Zealand', 'Kenya')
    aSport.addMatch(2018, APRIL, 13, 17, 30, 'B', 'Fiji', 'England')
    aSport.addMatch(2018, APRIL, 13, 17, 30, 'B', 'Australia', 'Wales')
    aSport.addMatch(2018, APRIL, 13, 18, 30, 'A', 'Canada', 'Kenya')
    aSport.addMatch(2018, APRIL, 13, 18, 30, 'A', 'New Zealand', 'South Africa')
    aSport.addMatch(2018, APRIL, 13, 19, 30, 'B', 'Fiji', 'Wales')
    aSport.addMatch(2018, APRIL, 13, 19, 30, 'B', 'Australia', 'England')

    aSport.addMatch(2018, APRIL, 14, 13, 30, 'A', 'South Africa', 'Kenya')
    aSport.addMatch(2018, APRIL, 14, 13, 30, 'A', 'New Zealand', 'Canada')
    aSport.addMatch(2018, APRIL, 14, 18, 30, 'B', 'England', 'Wales')
    aSport.addMatch(2018, APRIL, 14, 18, 30, 'B', 'Australia', 'Fiji')

    return the2018Games
  }
}