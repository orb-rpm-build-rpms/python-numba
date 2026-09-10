Name:           python-numba
Version:        0.65.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        compiling Python code using LLVM

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://numba.pydata.org
Source:         %{pypi_source numba}

BuildRequires:  python3-devel
BuildRequires:  gcc
# numba builds the _dispatcher C++ extension (numba/_dispatcher.cpp), so g++ is
# required in addition to the C compiler.
BuildRequires:  gcc-c++


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'numba' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-numba
Summary:        %{summary}

%description -n python3-numba %_description


%prep
%autosetup -p1 -n numba-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Automatically extracted from wheel
%pyproject_save_files -l numba


%check
# Exclude optional modules that import unavailable backends: the CUDA test suite
# (needs a CUDA toolchain/driver), the gdb pretty-printer and dump_style helper,
# the Jupyter notebook test helper, and the distutils/setuptools pycc usecases.
# None are used at runtime by our consumers.
%pyproject_check_import -e 'numba.cuda.tests.*' -e numba.misc.dump_style -e numba.misc.gdb_print_extension -e numba.testing.notebook -e 'numba.tests.pycc_distutils_usecase.*'


%files -n python3-numba -f %{pyproject_files}


%changelog
%autochangelog
