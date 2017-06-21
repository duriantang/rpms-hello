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
%find_lang %{name}
rm -f %{buildroot}/%{_infodir}/dir

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun
if [ $1 = 0 ] ; then
/sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_bindir}/hello
%{_infodir}/hello.info.*
%{_mandir}/man1/hello.1.*



%changelog
* Thu Jun 15 2017 Hui Tang <duriantang@gmail.com> - 2.10-1
- Initial version of the package
