from DotaApi.Heroes import Heroes
from DotaApi.constants import positions
class Reports:
    
    @staticmethod
    def create_match_report(match):
        '''
        params
        :match: Match object
        '''
        victory_team = 'Radiant' if match.match_info['radiant_win'] else 'Dire'
        first_blood_time = int(match.match_info['first_blood_time'] / 60)
        match_duration = int(match.match_info['duration'] / 60)
        radiant_heroes = Reports._get_heroes_by_team(match['players'], True)
        dire_heroes = Reports._get_heroes_by_team(match['players'], False)
        
        return {
            'victory_team' : victory_team,
            'first_blood_time' : first_blood_time,
            'match_duration' : match_duration,
            'radiant_heroes' : radiant_heroes,
            'dire_heroes' : dire_heroes
        }

    @staticmethod
    def _get_heroes_by_team(players, is_radiant):
        '''
        Get heroes and positions from a list of players in a match
        ''' 
        heroes = [{'hero': Heroes().get_hero_by_id(p['hero_id']), 'position': positions[str(p['lane_role'])]} for p in players if p['isRadiant'] == is_radiant]
        return heroes

    @staticmethod
    def create_player_match_report(match, player):
        '''
        Return the Player Performance in a Match
        '''
        # last hits
        # denies
        # kills
        # deaths
        # assists
        # win
        # hero
        # lane_role
        # multi-kill

        player_performance = next([p for p in match['players'] if p['account_id'] == player['account_id']], None)
        if player_performance is None:
            raise Exception('Player did not play match.')
        else:
            {
                'last_hits' : player_performance['last_hits'],
                'denies' : player_performance['denies'],
                'deaths' : player_performance['deaths'],
                'kills' : player_performance['kills'],
                'assists' : player_performance['assists'],
                'win' : player_performance['win'],
                'hero' : Heroes().get_hero_by_id(player_performance['hero_id']),
                'position': positions[str(player_performance['lane_role'])],
                'multi_kill' : player_performance['multi_kill']
            }


