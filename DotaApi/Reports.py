from DotaApi.Heroes import Heroes
from DotaApi.constants import positions
from datetime import datetime

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
        start_time = datetime.fromtimestamp(int(match.match_info['start_time']))
        radiant_heroes = Reports._get_heroes_by_team(match.match_info['players'], True)
        dire_heroes = Reports._get_heroes_by_team(match.match_info['players'], False)
        
        return {
            'victory_team' : victory_team,
            'first_blood_time' : first_blood_time,
            'match_duration' : match_duration,
            'radiant_heroes' : radiant_heroes,
            'dire_heroes' : dire_heroes,
            'match_date': str(start_time).split(' ')[0]
        }

    @staticmethod
    def _get_heroes_by_team(players, is_radiant):
        '''
        Get heroes and positions from a list of players in a match
        ''' 
        heroes = [{'hero': Heroes().get_hero_by_id(p['hero_id'])['localized_name'], 'position': positions[str(p.get('lane_role',5))]} for p in players if p['isRadiant'] == is_radiant]
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
        player_performance = next((p for p in match.match_info['players'] if p['account_id'] == player.id), None)
        if player_performance is None:
            raise Exception('Player did not play match.')
        else:
            return {
                'last_hits' : player_performance['last_hits'],
                'gold_per_min' : player_performance['gold_per_min'],
                'xp_per_min' : player_performance['xp_per_min'],
                'denies' : player_performance['denies'],
                'deaths' : player_performance['deaths'],
                'kills' : player_performance['kills'],
                'assists' : player_performance['assists'],
                'win' : player_performance['win'],
                'hero' : Heroes().get_hero_by_id(player_performance['hero_id'])['localized_name'],
                'position': positions[str(player_performance.get('lane_role',5))],
                'multi_kills' : player_performance['multi_kills'],
                'tower_damage': player_performance['tower_damage'],
                'hero_damage': player_performance['hero_damage'],
                'match_duration' : int(match.match_info['duration'] / 60),
                'match_date': str(datetime.fromtimestamp(int(match.match_info['start_time']))).split(' ')[0]
            }

    @staticmethod
    def player_stats(report):
        msg = f'[{report["match_date"]}][{report["match_duration"]}m] {report["hero"]} - {report["kills"]} cagadas / {report["deaths"]} mamadas / {report["assists"]} tentativas de ks.'
        return msg
    @staticmethod
    def player_match_report_msg(report):
        msg = f'[{report["match_date"]}][{report["match_duration"]}m] {report["hero"]} - {report["kills"]}/{report["deaths"]}/{report["assists"]} - '
        msg += f'LH:{report["last_hits"]} - DN:{report["denies"]} - HD:{report["hero_damage"]} - TD:{report["tower_damage"]} - GPM:{report["gold_per_min"]} - XPM:{report["xp_per_min"]} - {"Venceu" if int(report["win"])==1 else "Perdeu"}' 
        return msg
    
    @staticmethod
    def player_matches_summary_msg(player_name, reports):

        win_cnt = sum(int(r["win"]) for r in reports)
        lose_cnt = len(reports) - win_cnt

        msg = f'{player_name} está com {win_cnt} vitória(s) e {lose_cnt} derrota(s).'
        return msg



