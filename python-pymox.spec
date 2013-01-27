# TODO: rename to python-mox to conform to pld python package naming policy (python-MODULE_NAME)
%define 	module	pymox
Summary:	Mox is a mock object framework for Python
Name:		python-%{module}
Version:	0.5.3
Release:	2
License:	Apache
Group:		Libraries/Python
Source0:	http://pymox.googlecode.com/files/mox-%{version}.tar.gz
# Source0-md5:	2c43da56ed1bbbbf7805e81c76a924cc
URL:		https://code.google.com/p/pymox/
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mox is based on EasyMock, a Java mock object framework.

Mox will make mock objects for you, so you don't have to create your
own! It mocks the public/protected interfaces of Python objects. You
set up your mock objects expected behavior using a domain specific
language (DSL), which makes it easy to use, understand, and refactor!

%prep
%setup -q -n mox-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/*.egg-info
