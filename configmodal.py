
from discord import ui
import discord
from discord.interactions import Interaction
import os

class ConfigModal(ui.Modal):
    sheet_name = ui.TextInput(label="Sheet Name",placeholder="Enter your sheet name", style= discord.TextStyle.short)
    columns = ui.TextInput(label="Columns",placeholder="Enter your columns in order", style= discord.TextStyle.short)
    context = ui.TextInput(label="Context",placeholder="Enter your context", style= discord.TextStyle.long)

    async def on_submit(self, interaction: discord.Interaction):
       os.environ['A'] = self.sheet_name.value
       os.environ['B'] = self.context.value
       os.environ['C'] = self.columns.value

       message = f"""sheet name changed to **{self.sheet_name}**
context changed to **{self.context}**
columns changed to **{self.columns}**"""
       await interaction.response.send_message(message ,ephemeral=True)
    
