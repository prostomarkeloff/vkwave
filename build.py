from distutils.command.build_ext import build_ext


class BuildExt(build_ext):
    def build_extensions(self):
        try:
            super().build_extensions()
        except Exception:
            pass


def build(setup_kwargs):
    try:
        from Cython.Build import cythonize

        print("Building Cython extension...")

        setup_kwargs.update(
            dict(
                ext_modules=cythonize(["vkwave/bots/core/dispatching/filters/builtin_cyth.pyx"]),
                cmdclass=dict(build_ext=BuildExt),
            )
        )
    except Exception:
        print("Can't build Cython extension, using pure Python...")
