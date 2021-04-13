import discord
import os
import argparse
from DotaApi.Matches import Matches
from DotaApi.Players import Player
from DotaApi.Heroes import Heroes
from DotaApi.Reports import Reports
players = {
    'Eder' : 105273970,
    'Raphael' : 87239215,
    'Jubinha' : 87353829,
    'Will' : 97264439,
    'Peu' : 154813282,
    'Ze' : 204133988,
    'Boreah': 83967899
}
player_list = ['Eder', 'Raphael', 'Jubinha', 'Will', 'Peu', 'Ze', 'Boreah']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('DOTA stats'): #DOTA matches Jubinha 10
            try:
                player = message.content.split(' ')[2]
            except:
                message.channel.send(f"Erro, comando inválido. Tente 'DOTA stats PLAYER'")
                return
            if len(message.content.split(' ')) == 3:
                days_ago = 1
            else:
                days_ago = int(message.content.split(' ')[3])
            if player not in player_list:
                await message.channel.send(f"Erro, somente os players: {', '.join(player_list)}")
                return
            else:
                player_obj = Player(name=player, id=players[player])
                matches = player_obj.get_matches(limit=days_ago)
                reports = []
                for m in matches:
                    reports.append(Reports.create_player_match_report(Matches(int(m['match_id'])), player_obj))
                msg = Reports.player_matches_summary_msg(player, reports) + '\n'
                msg += "\n".join([Reports.player_stats(r) for r in reports])
                await message.channel.send(msg)
                return 

        if message.content.startswith('DOTA matches'): #DOTA matches Jubinha 10
            try:
                player = message.content.split(' ')[2]
            except:
                message.channel.send(f"Erro, comando inválido. Tente 'DOTA stats PLAYER'")
                return
            if len(message.content.split(' ')) == 3:
                days_ago = 1
            else:
                days_ago = int(message.content.split(' ')[3])
            if player not in player_list:
                await message.channel.send(f"Erro, somente os players: {', '.join(player_list)}")
                return
            else:
                player_obj = Player(name=player, id=players[player])
                matches = player_obj.get_matches(limit=days_ago)
                reports = []
                for m in matches:
                    reports.append(Reports.create_player_match_report(Matches(int(m['match_id'])), player_obj))
                msg = Reports.player_matches_summary_msg(player, reports) + '\n'
                msg += "\n".join([Reports.player_match_report_msg(r) for r in reports])
                await message.channel.send(msg)
                return 
        if message.content.startswith('DOTA heroes'): #DOTA heroes Jubinha hero
            try:
                player = message.content.split(' ')[2]
            except:
                message.channel.send(f"Erro, comando inválido. Tente 'DOTA heroes PLAYER hero'")
                return
            if len(message.content.split(' ')) == 3:
                await message.channel.send(f"Erro, heroi não informado.")
                return
            else:
                hero = message.content.split(' ',3)[3]
            if player not in player_list:
                await message.channel.send(f"Erro, somente os players: {', '.join(player_list)}")
                return
            else:
                player_obj = Player(name=player, id=players[player])
                try:
                    hero = Heroes().get_hero_by_name(hero_name=hero)
                except:
                    await message.channel.send(f"Erro! Escreve o nome do hero direito, animal.")
                    return
                reports = []
                matches = player_obj.get_matches(hero_id=hero['id'], limit=10)
                for m in matches:
                    reports.append(Reports.create_player_match_report(Matches(int(m['match_id'])), player_obj))
                msg = Reports.player_matches_summary_msg(player, reports) + '\n'
                msg += "\n".join([Reports.player_match_report_msg(r) for r in reports])
                await message.channel.send(msg)
                return


                
                
client = MyClient()
client.run(os.environ['BOT_TOKEN'])