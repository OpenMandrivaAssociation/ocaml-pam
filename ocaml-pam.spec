%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	OCamlPAM is a wrapper for the Pluggable Authentication Modules (PAM) library
Name:		ocaml-pam
Version:	1.1
Release:	3
License:	MIT
Group:		Development/Other
Url:		http://sharvil.nanavati.net/projects/ocamlpam/
Source0:	http://sharvil.nanavati.net/projects/ocamlpam/files/ocamlpam-%{version}.tar.gz
BuildRequires:	ocaml
BuildRequires:	pam-devel

%description
OCamlPAM is a wrapper for the Pluggable Authentication Modules (PAM)
library. PAM provides a flexible mechanism for authenticating users via
administrator-defined policies. PAM has modules for authenticating via
Unix passwd files, Kerberos, LDAP, etc. Additional modules for custom
authentication mechanisms can be created and deployed without recompiling
existing services based on PAM. Moreover, policies defining the
authentication requirements can be changed at runtime without restarting
running services.

%files
%doc COPYING CHANGES README
%dir %{_libdir}/ocaml/pam
%{_libdir}/ocaml/pam/META
%{_libdir}/ocaml/pam/*.cma
%{_libdir}/ocaml/pam/*.cmi
%{_libdir}/ocaml/stublibs/*.so*

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%{_libdir}/ocaml/pam/*.a
%{_libdir}/ocaml/pam/*.cmxa
%{_libdir}/ocaml/pam/*.cmx
%{_libdir}/ocaml/pam/*.mli

#----------------------------------------------------------------------------

%prep
%setup -q -n ocamlpam-%{version}

%build
make all opt

%install
make install DESTDIR=%{buildroot}%{_libdir}/ocaml/

