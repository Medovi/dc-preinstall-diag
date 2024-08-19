%define _unpackaged_files_terminate_build 1
Name: alterator-diag-domain-controller-pre-create
Version: 0.0.1
Release: alt1

Summary: A system health diagnostic tool before installing the first domain controller.
License: GPLv3
Group: Other
URL: https://github.com/Medovi/dc-preinstall-diag.git
BuildArch: noarch
Source0: %name-%version.tar

%description
A system health diagnostic tool before installing the first domain controller.

%prep
%setup

%build
sed -i 's/^VERSION=.*/VERSION=%version/' %name

%install
mkdir -p %buildroot%_alterator_datadir/diagnostictools/%name

install -p -D -m755 %name %buildroot%_bindir/%name
install -p -D -m644 %name.backend %buildroot%_alterator_datadir/backends/%name.backend
install -p -D -m644 %name.diagnostictool %buildroot%_alterator_datadir/diagnostictools/%name/%name.diagnostictool
install -p -D %name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

%files
%_bindir/%name
%_alterator_datadir/backends/%name.backend
%_alterator_datadir/diagnostictools/%name/%name.diagnostictool
%_iconsdir/hicolor/scalable/apps/%name.svg

