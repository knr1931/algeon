mdarray_sources = [
    './src/mdarraymodule.cpp',
]

mdarray_include_directories = [
    './src',
]

py.extension_module(
    'matrix',
    mdarray_sources,
    include_directories: mdarray_include_directories,
    install: true,
)

python_sources = [
  '__init__.py',
  'matrixobject.py',
  '_matypes.py',
]

py.install_sources(
  python_sources,
  subdir: 'nwengine/matrix'
)