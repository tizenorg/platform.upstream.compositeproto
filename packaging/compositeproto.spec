#
# Please submit bugfixes or comments via http://bugs.tizen.org/
#

Name:           compositeproto
Version:        0.4.2
Release:        1
License:        MIT
Summary:        X
Url:            http://www.x.org
Group:          Development/System
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros)

%description
%{summary}.

%prep
%setup -q

%build
%configure --disable-static \
             --libdir=%{_datadir} \
             --without-xmlto

make %{?_smp_mflags}

%install
%make_install

%remove_docs


%files
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/*
%{_datadir}/pkgconfig/*

