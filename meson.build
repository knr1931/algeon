project(
    'nweng',
    'c', 'cpp', 'cython',
    version: '1.0',
    default_options: [
    'buildtype=debugoptimized',
    'b_ndebug=if-release',
    'c_std=c99',
    'cpp_std=c++17',
    'pkgconfig.relocatable=true',
  ],
)

cc = meson.get_compiler('c')
cpp = meson.get_compiler('cpp')
cy = meson.get_compiler('cython')

# Check compiler is recent enough
if cc.get_id() == 'gcc'
  if not cc.version().version_compare('>=13.2')
    error('nweng requires GCC >= 13.2')
  endif
elif cc.get_id() == 'msvc'
  if not cc.version().version_compare('>=19.20')
    error('nweng requires at least vc142 (default with Visual Studio 2019) ' + \
          'when building with MSVC')
  endif
endif
if not cy.version().version_compare('>=3.0.2')
  error('nweng requires Cython >=3.0.2')
endif

#Python Module
py = import('python').find_installation(pure: false)
py_dep = py.dependency()

if not cc.has_header('Python.h', dependencies: py_dep)
  error('Cannot compile `Python.h`. Perhaps you need to install python-dev|python-devel')
endif


# Add default compile flags for any compiler that supports them.

subdir('nweng')