%define 	module	pymox
Summary:	Mox is a mock object framework for Python
Name:		python-%{module}
Version:	0.5.0
Release:	1
License:	Apache
Group:		Libraries/Python
Source0:	http://pymox.googlecode.com/files/mox-%{version}.tar.gz
# Source0-md5:	4203ea4f03c7dcec0a1ceb1290a8b615
URL:		http://pyme.sourceforge.net/
%pyrequires_eq	python-modules
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
export CFLAGS="%{rpmcflags}"
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name '*.py' | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/*.egg-info
