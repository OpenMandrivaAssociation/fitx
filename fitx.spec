Name:		fitx
Version:	0.5.0
Release:	%mkrel 1
Summary:	Fun Input Toy for Linux
License:	New BSD License
Group:		System/Internationalization
URL:		http://code.google.com/p/fitx/
Source0:	http://fitx.googlecode.com/files/%{name}_%{version}_beijing2008.src.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	scim-python
BuildRequires:	gnustep-base-devel
BuildRequires:	gnustep-make
BuildRequires:	sqlite3-devel
BuildRequires:	openssl-devel
Requires:	scim-python

%description
Fun Input Toy for Linux.

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc debian/changelog debian/README
%{_bindir}/*
%{_datadir}/scim-python/engine/FunInputToy
%{_datadir}/scim-python/setupui/FunInputToy
%{_datadir}/fit
#-----------------------------------------------------------

%prep
%setup -q -n %{name}_%{version}

%build
. /usr/share/GNUstep/Makefiles/GNUstep.sh
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT
