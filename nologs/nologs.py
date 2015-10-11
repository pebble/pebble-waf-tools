"""
Use this tool in conjunction with the following code in your primary C file (following #include <pebble.h>) to
include/exclude logs based on whether a build is passed the --no-log flag:

#if NOLOG
#undef APP_LOG
#define APP_LOG(...)
#endif
"""


def options(ctx):
    ctx.add_option('--no-log', action='store_true',
                   help="Mark a build to exclude app logging output")

def configure(ctx):
    if ctx.options.no_log:
        ctx.env.append_unique('DEFINES', 'NOLOG')
