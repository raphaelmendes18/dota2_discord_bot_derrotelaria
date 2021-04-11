import discord
import os
import argparse
from DotaApi.Matches import Matches
from DotaApi.Players import Players
from DotaApi.Heroes import Heroes

players = {
    'Eder' : 105273970,
    'Raphael' : 87239215,
    'Jubinha' : 87353829,
    'Will' : 97264439,
    'Peu' : 154813282,
    'Ze' : 204133988
}
player_list = ['Eder', 'Raphael', 'Jubinha', 'Will', 'Peu', 'Ze']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return
        
        if message.content.startswith('DOTA stats'):
            count_wins = 0
            player = message.content.split(' ')[2]
            if player not in player_list:
                await message.channel.send(f"Erro, somente os players: {', '.join(player_list)}")
            else:
                msg = ''
                matches = Players().get_player_matches(players[player], date=1)
                if len(matches) == 0:
                    await message.channel.send(f'{player} não mamou hoje.', tts=True)
                    return
                for match in matches:
                    hero = Heroes().get_hero_by_id(match['hero_id'])
                    if match['player_slot'] < 100:
                        win = match['radiant_win'] == 1
                        count_wins += 1
                    else:
                        win = match['radiant_win'] == 0
                    
                    msg += f'{player} jogou de {hero["localized_name"]}, mamou {match["deaths"]} {"vezes" if match["deaths"] > 1 else "vez"} e {"venceu" if win else "perdeu de novo"}.\n'
                
                msg += f'Saldo das últimas 24h: {count_wins} vitória(s) e {len(matches) - count_wins} derrota(s).'
                await message.channel.send(msg)
                if player == 'Ze':
                    await message.channel.send('MaMaMaMamou mumumuito hoje!!!', tts=True)
client = MyClient()
client.run(os.environ['BOT_TOKEN'])

# print(Matches().get_match_by_id(5936727209))


# # BOREAH = 

# if __name__=='__main__':
#     arg_parser = argparse.ArgumentParser()
#     arg_parser.add_argument('--player_name', required=True, type=str)
#     arg_parser.add_argument('--days_ago', required=True, type=int)

#     arguments = arg_parser.parse_args()
    
#     matches = Players().get_player_matches(players[arguments.player_name], date=arguments.days_ago)
#     for match in matches:
#         hero = Heroes().get_hero_by_id(match['hero_id'])
#         print(f'{arguments.player_name} jogou de {hero["localized_name"]} e mamou {match["deaths"]} {"vez(es)" if match["deaths"] > 1 else "vez"}.')
