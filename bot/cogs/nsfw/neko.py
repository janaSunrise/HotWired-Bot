from random import choice

import discord
import requests
from discord.ext import commands


async def make_embed(img: str, provider: str, author: discord.User):
    em = discord.Embed(color=discord.Colour.red())
    em.title = provider + " requested by " + author.name
    em.set_image(url=img)
    return em


class NSFW(commands.Cog):
    conf = {}

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    async def get(self, url, author: discord.User):
        base = 'https://api.nekos.dev/api/v3/'
        r = requests.get(base + url)
        r = r.json()
        em = await make_embed(r['data']['response']["url"], "Nekos.life", author)
        return em

    @commands.group()
    @commands.guild_only()
    async def neko(self, ctx):
        """Query sources from nekos.life!"""
        if ctx.invoked_subcommand is None:
            await ctx.invoke(self.sfw_neko)

    @neko.command(name='neko')
    @commands.guild_only()
    async def sfw_neko(self, ctx):
        async with ctx.typing():
            sources = ["images/sfw/img/neko", "images/sfw/gif/neko"]
            source = choice(sources)
            em = await self.get(source, ctx.author)
            msg: discord.Message = await ctx.send(embed=em)
            await msg.add_reaction("😻")

    @neko.command(name='nsfw')
    @commands.guild_only()
    @commands.is_nsfw()
    async def nsfw_neko(self, ctx):
        sources = ["images/nsfw/gif/neko", "images/nsfw/img/neko_lewd", "images/nsfw/img/neko_ero"]
        source = choice(sources)
        em = await self.get(source, ctx.author)
        msg = await ctx.send(embed=em)
        await msg.add_reaction("😻")

    @neko.command(name="waifu")
    @commands.guild_only()
    async def sfw_waifu(self, ctx):
        async with ctx.typing():
            source = "images/sfw/img/waifu"
            em = await self.get(source, ctx.author)
            msg: discord.Message = await ctx.send(embed=em)
            await msg.add_reaction("❤️")

    @neko.command(name="kitsune")
    @commands.guild_only()
    async def sfw_kitsune(self, ctx):
        async with ctx.typing():
            source = "images/sfw/img/kitsune"
            em = await self.get(source, ctx.author)
            msg: discord.Message = await ctx.send(embed=em)
            await msg.add_reaction("❤️")

    @neko.command(name="lewd")
    @commands.guild_only()
    @commands.is_nsfw()
    async def nsfw_classic(self, ctx):
        sources = ["images/nsfw/img/classic_lewd", "images/nsfw/img/neko_lewd", "images/nsfw/img/neko_ero"]
        source = choice(sources)
        em = await self.get(source, ctx.author)
        msg: discord.Message = await ctx.send(embed=em)
        await msg.add_reaction("😻")

    @neko.command(name="blowjob")
    @commands.guild_only()
    @commands.is_nsfw()
    async def nsfw_blowjob(self, ctx):
        sources = ["images/nsfw/gif/blow_job", "images/nsfw/img/blowjob_lewd"]
        source = choice(sources)
        em = await self.get(source, ctx.author)
        msg: discord.Message = await ctx.send(embed=em)
        await msg.add_reaction("❤️")

    @neko.command(name="furry")
    @commands.guild_only()
    @commands.is_nsfw()
    async def nsfw_furry(self, ctx):
        sources = ["images/nsfw/gif/yiff", "images/nsfw/img/yiff_lewd"]
        source = choice(sources)
        em = await self.get(source, ctx.author)
        msg: discord.Message = await ctx.send(embed=em)
        await msg.add_reaction("❤️")

    @neko.command(name="pussy")
    @commands.guild_only()
    @commands.is_nsfw()
    async def nsfw_pussy(self, ctx):
        sources = ["images/nsfw/gif/pussy_wank", "images/nsfw/gif/pussy", "images/nsfw/img/pussy_lewd"]
        source = choice(sources)
        em = await self.get(source, ctx.author)
        msg: discord.Message = await ctx.send(embed=em)
        await msg.add_reaction("❤️")

    @neko.command(name="feet")
    @commands.guild_only()
    @commands.is_nsfw()
    async def nsfw_feet(self, ctx):
        sources = ["images/nsfw/gif/feet", "images/nsfw/img/feet_lewd", "images/nsfw/img/feet_ero"]
        source = choice(sources)
        em = await self.get(source, ctx.author)
        msg: discord.Message = await ctx.send(embed=em)
        await msg.add_reaction("🥿🦶🦶🦶🦵🦵🦶🐾🦶🐾👟❤️")

    @neko.command(name="yuri")
    @commands.guild_only()
    @commands.is_nsfw()
    async def nsfw_yuri(self, ctx):
        sources = ["images/nsfw/gif/yuri", "images/nsfw/img/yuri_lewd", "images/nsfw/img/yuri_ero"]
        source = choice(sources)
        em = await self.get(source, ctx.author)
        msg: discord.Message = await ctx.send(embed=em)
        await msg.add_reaction("❤️")

    @neko.command(name="solo")
    @commands.guild_only()
    @commands.is_nsfw()
    async def nsfw_solo(self, ctx):
        sources = ["images/nsfw/gif/girls_solo", "images/nsfw/img/solo_lewd"]
        source = choice(sources)
        em = await self.get(source, ctx.author)
        msg: discord.Message = await ctx.send(embed=em)
        await msg.add_reaction("❤️")

    @neko.command(name="cum")
    @commands.guild_only()
    @commands.is_nsfw()
    async def nsfw_cum(self, ctx):
        sources = ["images/nsfw/gif/cum", "images/nsfw/img/cum_lewd"]
        source = choice(sources)
        em = await self.get(source, ctx.author)
        msg: discord.Message = await ctx.send(embed=em)
        await msg.add_reaction("❤️")

    @neko.command(name="cunni")
    @commands.guild_only()
    @commands.is_nsfw()
    async def nsfw_cunni(self, ctx):
        source = "images/nsfw/gif/kuni"
        em = await self.get(source, ctx.author)
        msg: discord.Message = await ctx.send(embed=em)
        await msg.add_reaction("❤️")

    @neko.command(name="bdsm")
    @commands.guild_only()
    @commands.is_nsfw()
    async def nsfw_bdsm(self, ctx):
        source = "images/nsfw/img/bdsm_lewd"
        em = await self.get(source, ctx.author)
        msg: discord.Message = await ctx.send(embed=em)
        await msg.add_reaction("❤️")

    @neko.command(name="trap")
    @commands.guild_only()
    @commands.is_nsfw()
    async def nsfw_trap(self, ctx):
        sources = ["images/nsfw/img/trap_lewd", "images/nsfw/img/futanari_lewd"]
        source = choice(sources)
        em = await self.get(source, ctx.author)
        msg: discord.Message = await ctx.send(embed=em)
        await msg.add_reaction("❤️")

    @neko.command(name="femdom")
    @commands.guild_only()
    @commands.is_nsfw()
    async def nsfw_femdom(self, ctx):
        source = "images/nsfw/img/femdom_lewd"
        em = await self.get(source, ctx.author)
        msg: discord.Message = await ctx.send(embed=em)
        await msg.add_reaction("❤️")


def setup(bot):
    bot.add_cog(NSFW(bot))