%define _unpackaged_files_terminate_build 1
Name: dc-preinstall-diag
Version: 0.0.1
Release: alt1

Summary: A tool to check the system status before installing a domain controller.
License: GPLv3
Group: Other
URL: https://github.com/Medovi/dc-preinstall-diag/tree/main
BuildArch: noarch
Source0: %name-%version.tar

%description
A tool to check the system status before installing a domain controller.

%prep
%setup

%build
sed -i 's/^VERSION=.*/VERSION=%version/' %name

%install
mkdir -p %buildroot%_alterator_datadir/diagnostictools/%name

install -p -D -m755 %name %buildroot%_bindir/%name
install -p -D -m644 %name.backend %buildroot%_alterator_datadir/backends/%name.backend
install -p -D -m644 %name.diagnostictool %buildroot%_alterator_datadir/diagnostictools/%name/%name.diagnostictool

%files
%_bindir/%name
%_alterator_datadir/backends/%name.backend
%_alterator_datadir/diagnostictools/%name/%name.diagnostictool

%changelog
* Sun Aug 08 2024 Sergey Savelev <savelevsa@basealt.ru> 0.0.1-alt1
- initial build

