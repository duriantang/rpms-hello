Name:           hello
Version:
Release:        1%{?dist}
Summary:

License:
URL:
Source0:

BuildRequires:
Requires:

%description


%prep
%autosetup


%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license add-license-file-here
%doc add-docs-here



%changelog
* Thu Jun 15 2017 Hui Tang <duriantang@gmail.com>
-
