#
# spec file for package monitoring-check_mem
#

Name:           monitoring-check_mem
Version:        %{version}
Release:        %{release}
Summary:        Check System memory
License:        MIT
Group:          System/Monitoring
Url:            http://sysadminsjourney.com/content/2009/06/04/new-and-improved-checkmempl-nagios-plugin/
Source0:        monitoring-check_mem-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl
Provides:       check_mem

%description
Revision of check_mem.pl that splits out cache memory from application memory -
see http://sysadminsjourney.com/content/2009/06/04/new-and-improved-checkmempl-nagios-plugin

%prep
%setup -q -n monitoring-check_mem-%{version}

%install
mkdir -p "$RPM_BUILD_ROOT/usr/lib64/nagios/plugins"
cp "check_mem/check_mem.pl" "$RPM_BUILD_ROOT/usr/lib64/nagios/plugins/"

%files
%defattr(-,root,root,755)
%attr(0755,root,root) /usr/lib64/nagios/plugins/check_mem.pl

%changelog
* Thu Apr 28 2022 Joern Ott <joern.ott@ott-consult.de>
- Initial version
