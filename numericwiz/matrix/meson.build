mdarray_sources = [
    './src/mdarraymodule.cpp',
]

mdarray_include_directories = [
    './src',
]

py.extension_module(
    'matrix',
    mdarray_sources,
    include_directories: [mdarray_include_directories,incdir_numpy],
    install: true,
)

python_sources = [
  '__init__.py',
  'matrixobject.py',
  '_matypes.py',
  '_typing.py',
]

py.install_sources(
  python_sources,
  subdir: 'numericwiz/matrix'
)

install_subdir('tests', install_dir: numericwiz_dir / 'matrix')