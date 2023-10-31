# subdir('linopt')

nwengine_sources = [
    './src/marraymodule.cpp',
]

nwengine_include_directories = [
    './src',
]

py.extension_module(
    'marraymodule',
    nwengine_sources,
    include_directories: nwengine_include_directories,
    install: true,
)