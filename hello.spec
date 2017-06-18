Name:           hello
Version:        2.10
Release:        1%{?dist}
Summary:        The "Hello World" program from GNU

License:        GPLv3+
URL:            https://ftp.gnu.org/gnu/%{name}
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz

# BuildRequires:
# Requires:

%description
The "Hello World" program, done with all bells and whistles of a proper FOSS
project, including configuration, build, internationalization, help files, etc.


%prep
%autosetup


%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license LICENSE
%doc add-docs-here



%changelog
* Thu Jun 15 2017 Hui Tang <duriantang@gmail.com> - 2.10-1
- Initial version of the package
