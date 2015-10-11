def configure(ctx):
    ctx.env.append_unique('CFLAGS', '-pedantic')
