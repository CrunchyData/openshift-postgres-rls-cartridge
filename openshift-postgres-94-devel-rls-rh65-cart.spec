%global cartridgedir %{_libexecdir}/openshift/cartridges/crunchypg-rls-cart

Summary:       Provides Crunchy Postgres 94devel rls support
Name:          openshift-postgres-94-devel-rls-rh65-cart
Version:       0.0.11
Release:       1%{?dist}
Group:         Development/Languages
License:       ASL 2.0
URL:           http://www.openshift.com
Source0:       file:///./%{name}-%{version}.tar.gz
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
Requires:      lsof
Requires:      bc
Requires:      /bin/sh

%description
Provides postgres 94 devel rls support to OpenShift. (Cartridge Format V2)

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%post

%{_sbindir}/oo-admin-cartridge --action install --source %{cartridgedir}


%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/hooks/
%{cartridgedir}
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/LICENSE

%changelog
* Wed Jul 02 2014 jeff mccormick <jeffmc04@gmail.com> 0.0.11-1
- commented out debugger (jeffmc04@gmail.com)

* Wed Jul 02 2014 jeff mccormick <jeffmc04@gmail.com> 0.0.10-1
- 

* Wed Jul 02 2014 jeff mccormick <jeffmc04@gmail.com> 0.0.9-1
- 

* Wed Jul 02 2014 jeff mccormick <jeffmc04@gmail.com> 0.0.8-1
- removed due to rename (jeffmc04@gmail.com)
- added (jeffmc04@gmail.com)

* Wed Jul 02 2014 jeff mccormick <jeffmc04@gmail.com> 0.0.7-1
- new package built with tito

* Tue Mar 18 2014 Unknown name 0.0.6-1
- fix (jeffmc@localhost.localdomain)

* Tue Mar 18 2014 Unknown name 0.0.5-1
- fix (jeffmc@localhost.localdomain)

* Tue Mar 18 2014 Unknown name 0.0.4-1
- fixed (jeffmc@localhost.localdomain)

* Tue Mar 18 2014 Unknown name 0.0.3-1
- fix spec (jeffmc@localhost.localdomain)

* Tue Mar 18 2014 Unknown name 0.0.2-1
- new package built with tito

