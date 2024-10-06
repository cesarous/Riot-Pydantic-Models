from enum import Enum
from pydantic import BaseModel, Field, root_validator
from typing import Optional, Union


class PlatformEnum(str, Enum):
    EUW1 = "euw1"
    EUN1 = "eun1"
    NA1 = "na1"
    KR = "kr"
    BR1 = "br1"
    LA1 = "la1"
    LA2 = "la2"
    OC1 = "oc1"
    TR1 = "tr1"
    RU = "ru"
    JP1 = "jp1"
    PH2 = "ph2"
    SG2 = "sg2"
    TH2 = "th2"
    TW2 = "tw2"
    VN2 = "vn2"

class TierEnum(str, Enum):
    IRON = "IRON"
    BRONZE = "BRONZE"
    SILVER = "SILVER"
    GOLD = "GOLD"
    EMERALD = "EMERALD"
    PLATINUM = "PLATINUM"
    DIAMOND = "DIAMOND"
    MASTER = "MASTER"
    GRANDMASTER = "GRANDMASTER"
    CHALLENGER = "CHALLENGER"

class RankEnum(str, Enum):
    I = "I"
    II = "II"
    III = "III"
    IV = "IV"

class TimelineEventEnum(str, Enum):
    ASCENDED_EVENT = "ASCENDED_EVENT"
    BUILDING_KILL = "BUILDING_KILL"
    CAPTURE_POINT = "CAPTURE_POINT"
    CHAMPION_KILL = "CHAMPION_KILL"
    CHAMPION_SPECIAL_KILL = "CHAMPION_SPECIAL_KILL"
    CHAMPION_TRANSFORM = "CHAMPION_TRANSFORM"
    DRAGON_SOUL_GIVEN = "DRAGON_SOUL_GIVEN"
    ELITE_MONSTER_KILL = "ELITE_MONSTER_KILL"
    GAME_END = "GAME_END"
    ITEM_DESTROYED = "ITEM_DESTROYED"
    ITEM_PURCHASED = "ITEM_PURCHASED"
    ITEM_SOLD = "ITEM_SOLD"
    ITEM_UNDO = "ITEM_UNDO"
    LEVEL_UP = "LEVEL_UP"
    OBJECTIVE_BOUNTY_PRESTART = "OBJECTIVE_BOUNTY_PRESTART"
    PAUSE_END = "PAUSE_END"
    PAUSE_START = "PAUSE_START"
    SKILL_LEVEL_UP = "SKILL_LEVEL_UP"
    TURRET_PLATE_DESTROYED = "TURRET_PLATE_DESTROYED"
    WARD_KILL = "WARD_KILL"
    WARD_PLACED = "WARD_PLACED"

class TeamIdEnum(int, Enum):
    BLUE = 100
    RED = 200


class SummonerDTO(BaseModel):
    ###    
        # SummonerDTO - represents a summoner
        # Name	Data Type	Description
        # accountId	string	Encrypted account ID. Max length 56 characters.
        # profileIconId	int	ID of the summoner icon associated with the summoner.
        # revisionDate	long	Date summoner was last modified specified as epoch milliseconds. The following events will update this timestamp: summoner name change, summoner level change, or profile icon change.
        # id	string	Encrypted summoner ID. Max length 63 characters.
        # puuid	string	Encrypted PUUID. Exact length of 78 characters.
        # summonerLevel	long	Summoner level associated with the summoner.
    ###
    id: str
    name: str
    revisionDate:int
    profileIconId: int
    puuid: str
    summonerLevel: int


class LeagueEntry(BaseModel):
    leagueId: str
    queueType: str
    tier: TierEnum
    rank: RankEnum
    summonerId: str
    summonerName: str
    leaguePoints: int
    wins: int
    losses: int
    hotStreak: bool
    veteran: bool
    freshBlood: bool
    inactive: bool
    miniSeries: Optional['miniSeriesDTO'] = None


class miniSeriesDTO(BaseModel):
    losses: int
    progress: str
    target: int
    wins: int


class MatchDTO(BaseModel):
    metadata: 'MetadataDTO'
    info: 'MatchInfoDTO'

class AbilityCastsDto(BaseModel):
    grenadeCasts:int	
    ability1Casts:int	
    ability2Casts:int	
    ultimateCasts:int

class PlayerStatsDto(BaseModel):
    score:int	
    roundsPlayed:int	
    kills:int	
    deaths:int	
    assists:int	
    playtimeMillis:int	
    abilityCasts:AbilityCastsDto

class PlayerDTO(BaseModel):
    puuid: str
    gameName: str
    tagLine:str
    teamId: str
    partyId:str
    characterId:str
    stats: PlayerStatsDto
    competitiveTier: int
    playerCard:str
    playerTitle:str

class CoachDTO(BaseModel):
    puuid:str	
    teamId:str

class TeamDTO(BaseModel):
    teamId:str	
    won:bool	
    roundsPlayed:int	
    roundsWon:int	
    numPoints:int

class LocationDto(BaseModel):
    x:int	
    y:int

class PlayerLocationsDto(BaseModel):
    puuid:str	
    viewRadians:float	
    location:LocationDto

class EconomyDto(BaseModel):
    loadoutValue:int	
    weapon:str	
    armor:str
    remaining:int	
    spent:int
class DamageDto(BaseModel):
    receiver:str
    damage:int	
    legshots:int	
    bodyshots:int	
    headshots:int

class FinishingDamageDto(BaseModel):
    damageType:str	
    damageItem:str	
    isSecondaryFireMode:bool

class KillDto(BaseModel):
    timeSinceGameStartMillis:int	
    timeSinceRoundStartMillis:int	
    killer:str
    victim:str
    victimLocation:LocationDto	
    assistants:list[str]
    playerLocations:list[PlayerLocationsDto]	
    finishingDamage:FinishingDamageDto	

class AbilityDto(BaseModel):
    grenadeEffects:str	
    ability1Effects:str	
    ability2Effects:str	
    ultimateEffects:str
    
class PlayerRoundStatsDto(BaseModel):
    puuid:str	
    kills:list[KillDto]	
    damage:list[DamageDto]	
    score:int	
    economy:EconomyDto	
    ability:AbilityDto


class RoundResultDto(BaseModel):
    roundNum:int	
    roundResult:str	
    roundCeremony:str	
    winningTeam:str	
    bombPlanter:str
    bombDefuser:str
    plantRoundTime:int	
    plantPlayerLocations:list[PlayerLocationsDto]	
    plantLocation:LocationDto	
    plantSite:str	
    defuseRoundTime:int	
    defusePlayerLocations:list[PlayerLocationsDto]	
    defuseLocation:LocationDto	
    playerStats:list[PlayerRoundStatsDto]	
    roundResultCode:str


class ValorantMatchDTO(BaseModel):
    matchInfo: 'MatchInfoDTO'
    players: list[PlayerDTO]
    coach: list[CoachDTO]
    teams: list[TeamDTO]
    roundResults: list[RoundResultDto]

class MetadataDTO(BaseModel):
    dataVersion: str
    matchId: str
    participants: list[str]

class MatchInfoDTO(BaseModel):
    endOfGameResult: str
    gameCreation: int
    gameDuration: int
    gameEndTimestamp: int
    gameId: int
    gameMode: str
    gameName: str
    gameStartTimestamp: int
    gameType: str
    gameVersion: str
    mapId: int
    participants: list['ParticipantDTO']
    platformId: str
    queueId: int
    teams: list['TeamDTO']
    tournamentCode: str

class ParticipantDTO(BaseModel):
    allInPings: int
    assistMePings: int
    assists: int
    baronKills: int
    basicPings: int
    bountyLevel: int
    challenges: 'ChallengesDTO'
    champExperience: int
    champLevel: int
    championId: int
    championName: str
    championTransform: int
    commandPings: int
    consumablesPurchased: int
    damageDealtToBuildings: int
    damageDealtToObjectives: int
    damageDealtToTurrets: int
    damageSelfMitigated: int
    dangerPings: int
    deaths: int
    detectorWardsPlaced: int
    doubleKills: int
    dragonKills: int
    eligibleForProgression: int
    enemyMissingPings: int
    enemyVisionPings: int
    firstBloodAssist: int
    firstBloodKill: int
    firstTowerAssist: int
    firstTowerKill: int
    gameEndedInEarlySurrender: int
    gameEndedInSurrender: int
    getBackPings: int
    goldEarned: int
    goldSpent: int
    holdPings: int
    individualPosition: str
    inhibitorKills: int
    inhibitorTakedowns: int
    inhibitorsLost: int
    item0: int
    item1: int
    item2: int
    item3: int
    item4: int
    item5: int
    item6: int
    itemsPurchased: int
    killingSprees: int
    kills: int
    lane: str
    largestCriticalStrike: int
    largestKillingSpree: int
    largestMultiKill: int
    longestTimeSpentLiving: int
    magicDamageDealt: int
    magicDamageDealtToChampions: int
    magicDamageTaken: int
    missions: 'MissionsDTO'
    needVisionPings: int
    neutralMinionsKilled: int
    nexusKills: int
    nexusLost: int
    nexusTakedowns: int
    objectivesStolen: int
    objectivesStolenAssists: int
    onMyWayPings: int
    participantId: int
    pentaKills: int
    perks: 'PerksDTO'
    physicalDamageDealt: int
    physicalDamageDealtToChampions: int
    physicalDamageTaken: int
    placement: int
    playerAugment1: int
    playerAugment2: int
    playerAugment3: int
    playerAugment4: int
    playerScore0: int
    playerScore1: int
    playerScore10: int
    playerScore11: int
    playerScore2: int
    playerScore3: int
    playerScore4: int
    playerScore5: int
    playerScore6: int
    playerScore7: int
    playerScore8: int
    playerScore9: int
    playerSubteamId: int
    profileIcon: int
    pushPings: int
    puuid: str
    quadraKills: int
    riotIdGameName: str
    riotIdTagline: str
    role: str
    sightWardsBoughtInGame: int
    spell1Casts: int
    spell2Casts: int
    spell3Casts: int
    spell4Casts: int
    subteamPlacement: int
    summoner1Casts: int
    summoner1Id: int
    summoner2Casts: int
    summoner2Id: int
    summonerId: str
    summonerLevel: int
    summonerName: str
    teamEarlySurrendered: int
    teamId: TeamIdEnum
    teamPosition: str
    timeCCingOthers: int
    timePlayed: int
    totalAllyJungleMinionsKilled: int
    totalDamageDealt: int
    totalDamageDealtToChampions: int
    totalDamageShieldedOnTeammates: int
    totalDamageTaken: int
    totalEnemyJungleMinionsKilled: int
    totalHeal: int
    totalHealsOnTeammates: int
    totalMinionsKilled: int
    totalTimeCCDealt: int
    totalTimeSpentDead: int
    totalUnitsHealed: int
    tripleKills: int
    trueDamageDealt: int
    trueDamageDealtToChampions: int
    trueDamageTaken: int
    turretKills: int
    turretTakedowns: int
    turretsLost: int
    unrealKills: int
    visionClearedPings: int
    visionScore: int
    visionWardsBoughtInGame: int
    wardsKilled: int
    wardsPlaced: int
    win: int

class ChallengesDTO(BaseModel):
    twelveAssistStreakCount: int = Field(alias="12AssistStreakCount")
    abilityUses: int
    acesBefore15Minutes: int
    alliedJungleMonsterKills: int
    baronTakedowns: int
    blastConeOppositeOpponentCount: int
    bountyGold: int
    buffsStolen: int
    completeSupportQuestInTime: int
    controlWardsPlaced: int
    damagePerMinute: float
    damageTakenOnTeamPercentage: float
    dancedWithRiftHerald: int
    deathsByEnemyChamps: int
    dodgeSkillShotsSmallWindow: int
    doubleAces: int
    dragonTakedowns: int
    earliestBaron: float
    earlyLaningPhaseGoldExpAdvantage: int
    effectiveHealAndShielding: float
    elderDragonKillsWithOpposingSoul: int
    elderDragonMultikills: int
    enemyChampionImmobilizations: int
    enemyJungleMonsterKills: int
    epicMonsterKillsNearEnemyJungler: int
    epicMonsterKillsWithin30SecondsOfSpawn: int
    epicMonsterSteals: int
    epicMonsterStolenWithoutSmite: int
    firstTurretKilled: int
    flawlessAces: int
    fullTeamTakedown: int
    gameLength: float
    getTakedownsInAllLanesEarlyJungleAsLaner: Optional[int] = None
    goldPerMinute: float
    hadOpenNexus: int
    immobilizeAndKillWithAlly: int
    initialBuffCount: int
    initialCrabCount: int
    jungleCsBefore10Minutes: float
    junglerTakedownsNearDamagedEpicMonster: int
    kTurretsDestroyedBeforePlatesFall: int
    kda: float
    killAfterHiddenWithAlly: int
    killParticipation: float
    killedChampTookFullTeamDamageSurvived: int
    killingSprees: int
    killsNearEnemyTurret: int
    killsOnOtherLanesEarlyJungleAsLaner: Optional[int] = None
    killsOnRecentlyHealedByAramPack: int
    killsUnderOwnTurret: int
    killsWithHelpFromEpicMonster: int
    knockEnemyIntoTeamAndKill: int
    landSkillShotsEarlyGame: int
    laneMinionsFirst10Minutes: int
    laningPhaseGoldExpAdvantage: int
    legendaryCount: int
    legendaryItemUsed: list[int]
    lostAnInhibitor: int
    maxCsAdvantageOnLaneOpponent: float
    maxKillDeficit: int
    maxLevelLeadLaneOpponent: int
    mejaisFullStackInTime: int
    moreEnemyJungleThanOpponent: float
    multiKillOneSpell: int
    multiTurretRiftHeraldCount: int
    multikills: int
    multikillsAfterAggressiveFlash: int
    outerTurretExecutesBefore10Minutes: int
    outnumberedKills: int
    outnumberedNexusKill: int
    perfectDragonSoulsTaken: int
    perfectGame: int
    pickKillWithAlly: int
    playedChampSelectPosition: int
    poroExplosions: int
    quickCleanse: int
    quickFirstTurret: int
    quickSoloKills: int
    riftHeraldTakedowns: int
    saveAllyFromDeath: int
    scuttleCrabKills: int
    skillshotsDodged: int
    skillshotsHit: int
    snowballsHit: int
    soloBaronKills: int
    soloKills: int
    soloTurretsLategame: Optional[int] = None
    stealthWardsPlaced: int
    survivedSingleDigitHpCount: int
    survivedThreeImmobilizesInFight: int
    takedownOnFirstTurret: int
    takedowns: int
    takedownsAfterGainingLevelAdvantage: int
    takedownsBeforeJungleMinionSpawn: int
    takedownsFirstXMinutes: int
    takedownsInAlcove: int
    takedownsInEnemyFountain: int
    teamBaronKills: int
    teamDamagePercentage: float
    teamElderDragonKills: int
    teamRiftHeraldKills: int
    tookLargeDamageSurvived: int
    turretPlatesTaken: int
    turretTakedowns: int
    turretsTakenWithRiftHerald: int
    twentyMinionsIn3SecondsCount: int
    twoWardsOneSweeperCount: int
    unseenRecalls: int
    visionScoreAdvantageLaneOpponent: float
    visionScorePerMinute: float
    wardTakedowns: int
    wardTakedownsBefore20M: int
    wardsGuarded: int

class MissionsDTO(BaseModel):
    playerScore0: int
    playerScore1: int
    playerScore10: int
    playerScore11: int
    playerScore2: int
    playerScore3: int
    playerScore4: int
    playerScore5: int
    playerScore6: int
    playerScore7: int
    playerScore8: int
    playerScore9: int

class PerksDTO(BaseModel):
    statPerks: 'StatPerksDTO'
    styles: list['StyleDTO']

class StatPerksDTO(BaseModel):
    defense: int
    flex: int
    offense: int

class StyleDTO(BaseModel):
    description: str
    selections: list['SelectionDTO']
    style: int

class SelectionDTO(BaseModel):
    perk: int
    var1: int
    var2: int
    var3: int

class TeamDTO(BaseModel):
    bans: list['BannedChampionDTO']
    objectives: 'ObjectivesDTO'
    teamId: TeamIdEnum
    win: bool

class BannedChampionDTO(BaseModel):
    championId: int
    pickTurn: int

class ObjectivesDTO(BaseModel):
    baron: 'ObjectiveDTO'
    champion: 'ObjectiveDTO'
    dragon: 'ObjectiveDTO'
    horde: 'ObjectiveDTO'
    inhibitor: 'ObjectiveDTO'
    riftHerald: 'ObjectiveDTO'
    tower: 'ObjectiveDTO'

class ObjectiveDTO(BaseModel):
    first: bool
    kills: int


class Timeline(BaseModel):
    metadata: 'MetadataDTO'
    info: 'TimelineInfoDTO'


class TimelineInfoDTO(BaseModel):
    endOfGameResult: str
    frameInterval: int
    frames: list['FrameDTO']
    gameId: int
    participants: list['TimelineParticipantDTO']

class FrameDTO(BaseModel):
    events: list[Union['AscendedEvent', 'BuildingKill', 'CapturePoint', 'ChampionKill', 'ChampionSpecialKill', 'ChampionTransform', 'DragonSoulGiven', 'EliteMonsterKill', 'GameEnd', 'ItemDestroyed', 'ItemPurchased', 'ItemSold', 'ItemUndo', 'LevelUp', 'ObjectiveBountyPrestart', 'PauseEnd', 'PauseStart', 'SkillLevelUp', 'TurretPlateDestroyed', 'WardKill', 'WardPlaced']]
    participantFrames: dict[str, 'ParticipantFrameDTO']
    timestamp: int

class VictimDamageDealtDTO(BaseModel):
    basic: bool
    magicDamage: int
    name: str
    participantId: int
    physicalDamage: int
    spellName: str
    spellSlot: int
    trueDamage: int
    type: str

class ParticipantFrameDTO(BaseModel):
    championStats: 'ChampionStatsDTO'
    currentGold: int
    damageStats: 'DamageStatsDTO'
    goldPerSecond: int
    jungleMinionsKilled: int
    level: int
    minionsKilled: int
    participantId: int
    position: 'PositionDTO'
    timeEnemySpentControlled: int
    totalGold: int
    xp: int

class ChampionStatsDTO(BaseModel):
    abilityHaste: int
    abilityPower: int
    armor: int
    armorPen: int
    armorPenPercent: int
    attackDamage: int
    attackSpeed: int
    bonusArmorPenPercent: int
    bonusMagicPenPercent: int
    ccReduction: int
    cooldownReduction: int
    health: int
    healthMax: int
    healthRegen: int
    lifesteal: int
    magicPen: int
    magicPenPercent: int
    magicResist: int
    movementSpeed: int
    omnivamp: int
    physicalVamp: int
    power: int
    powerMax: int
    powerRegen: int
    spellVamp: int

class DamageStatsDTO(BaseModel):
    magicDamageDone: int
    magicDamageDoneToChampions: int
    magicDamageTaken: int
    physicalDamageDone: int
    physicalDamageDoneToChampions: int
    physicalDamageTaken: int
    totalDamageDone: int
    totalDamageDoneToChampions: int
    totalDamageTaken: int
    trueDamageDone: int
    trueDamageDoneToChampions: int
    trueDamageTaken: int

class PositionDTO(BaseModel):
    x: int
    y: int

class TimelineParticipantDTO(BaseModel):
    participantId: int
    puuid: str

class BaseEvent(BaseModel):
    type: TimelineEventEnum
    timestamp: int

class AscendedEvent(BaseEvent):
    pass # TODO

class BuildingKill(BaseEvent):
    assistingParticipantIds: list[int]
    bounty: int
    buildingType: str
    killerId: int
    laneType: str
    position: PositionDTO
    teamId: TeamIdEnum
    towerType: str

class CapturePoint(BaseEvent):
    assistingParticipantIds: list[int]
    bounty: int
    killStreakLength: int
    killerId: int
    position: PositionDTO
    shutdownBounty: int
    victimDamageDealt: list[VictimDamageDealtDTO]
    victimDamageReceived: list[VictimDamageDealtDTO]
    victimId: int

class ChampionKill(BaseEvent):
    killType: str
    killerId: int
    position: PositionDTO

class ChampionSpecialKill(BaseEvent):
    killType: str
    killerId: int
    position: PositionDTO

class ChampionTransform(BaseEvent):
    participantId: int
    transformType: str

class DragonSoulGiven(BaseEvent):
    name: str
    teamId: TeamIdEnum

class EliteMonsterKill(BaseEvent):
    assistingParticipantIds: list[int]
    bounty: int
    killerId: int
    killerTeamId: TeamIdEnum
    monsterType: str
    position: PositionDTO

class GameEnd(BaseEvent):
    gameId: int
    realTimestamp: int
    winningTeam: int

class ItemDestroyed(BaseEvent):
    itemId: int
    participantId: int

class ItemPurchased(BaseEvent):
    itemId: int
    participantId: int

class ItemSold(BaseEvent):
    itemId: int
    participantId: int

class ItemUndo(BaseEvent):
    afterId: int
    beforeId: int
    goldGain: int
    participantId: int

class LevelUp(BaseEvent):
    level: int
    participantId: int

class ObjectiveBountyPrestart(BaseEvent):
    actualStartTime: int
    teamId: TeamIdEnum

class PauseEnd(BaseEvent):
    realTimestamp: int

class PauseStart(BaseEvent):
    realTimestamp: int

class SkillLevelUp(BaseEvent):
    levelUpType: str
    participantId: int
    skillSlot: int

class TurretPlateDestroyed(BaseEvent):
    killerId: int
    laneType: str
    position: PositionDTO
    teamId: TeamIdEnum

class WardKill(BaseEvent):
    killerId: int
    wardType: str

class WardPlaced(BaseEvent):
    creatorId: int
    wardType: int


class AccountDTO(BaseModel):
    puuid: str
    gameName:str
    tagLine:str