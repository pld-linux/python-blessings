#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		blessings
%define		egg_name	blessings
%define		pypi_name	blessings
Summary:	Python library for terminal coloring, styling, and positioning
Name:		python-%{module}
Version:	1.7
Release:	2
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	38555a2bba0ace706aec58444368e022
Patch1:		0001-fix-tests-when-run-without-a-tty-fixes-25.patch
Patch2:		0002-more-fixes-for-tests-without-a-tty.patch
URL:		https://github.com/erikrose/blessings
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-nose
BuildRequires:	python-setuptools
BuildRequires:	python-six
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-nose
BuildRequires:	python3-setuptools
BuildRequires:	python3-six
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Blessings is a thin, practical wrapper around terminal coloring,
styling, and positioning in Python.

%package -n python3-%{module}
Summary:	Python 3 library for terminal coloring, styling, and positioning
Group:		Libraries/Python

%description -n python3-%{module}
Blessings is a thin, practical wrapper around terminal coloring,
styling, and positioning in Python.

%prep
%setup -q -n %{pypi_name}-%{version}
%patch1 -p1
%patch2 -p1
rm -r blessings.egg-info

%build
%if %{with python2}
%py_build
%if %{with tests}
nosetests-%{py_ver} build-2/lib
%endif
%endif
%if %{with python3}
%py3_build
%if %{with tests}
nosetests-%{py3_ver} build-3/lib
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif
%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
