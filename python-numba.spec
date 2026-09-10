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
%pyproject_check_import


%files -n python3-numba -f %{pyproject_files}


%changelog
%autochangelog
