
Name:           obs-service-verify_file
License:        GPL v2 or later
Group:          Development/Tools/Building
Summary:        An OBS source service: file verification
Version:        0.1
Release:        1
Source:         verify_file
Source1:        verify_file.service
Requires:       coreutils
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

It allows to verify a file with a given sha256sum

%prep
%setup -q -D -T 0 -n .

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/obs/service
install -m 0755 %{SOURCE0} $RPM_BUILD_ROOT/usr/lib/obs/service
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT/usr/lib/obs/service

%files
%defattr(-,root,root)
%dir /usr/lib/obs
/usr/lib/obs/service

