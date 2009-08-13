Name:           ocaml-pam
Version:        1.1
Release:        %mkrel 1
Summary:        OCamlPAM is a wrapper for the Pluggable Authentication Modules (PAM) library
License:        MIT
Group:          Development/Other
URL:            http://sharvil.nanavati.net/projects/ocamlpam/
Source0:        http://sharvil.nanavati.net/projects/ocamlpam/files/ocamlpam-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
OCamlPAM is a wrapper for the Pluggable Authentication Modules (PAM)
library. PAM provides a flexible mechanism for authenticating users via
administrator-defined policies. PAM has modules for authenticating via
Unix passwd files, Kerberos, LDAP, etc. Additional modules for custom
authentication mechanisms can be created and deployed without recompiling
existing services based on PAM. Moreover, policies defining the
authentication requirements can be changed at runtime without restarting
running services.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ocamlpam-%{version}

%build
make all opt

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}%{_libdir}/ocaml/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING CHANGES README
%dir %{_libdir}/ocaml/pam
%{_libdir}/ocaml/pam/META
%{_libdir}/ocaml/pam/*.cma
%{_libdir}/ocaml/pam/*.cmi
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root)
%{_libdir}/ocaml/pam/*.a
%{_libdir}/ocaml/pam/*.cmxa
%{_libdir}/ocaml/pam/*.cmx
%{_libdir}/ocaml/pam/*.mli

