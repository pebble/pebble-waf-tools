def options(ctx):
    ctx.add_option('--jshint', action='store_true', help="Run JSHint on the JS files in the build")

def configure(ctx):
    if ctx.options.jshint:
        try:
            ctx.find_program('jshint', var='JSHINT')
        except ctx.errors.ConfigurationError:
            print "jshint was not found"

def build(ctx):
    if ctx.env.JSHINT:
        ctx(rule='${JSHINT} ${SRC}', source=ctx.path.ant_glob('src/**/*.js'), name='jshint')
