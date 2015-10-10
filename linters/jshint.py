def configure(ctx):
    ctx.find_program('jshint', var='JSHINT', mandatory=False)

def build(ctx):
    if ctx.env.JSHINT:
        ctx(rule='${JSHINT} ${SRC}', source=ctx.path.ant_glob('src/**/*.js'), name='jshint')
