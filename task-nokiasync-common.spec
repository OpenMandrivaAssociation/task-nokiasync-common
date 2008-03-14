Name:		task-nokiasync-common
Version:	1.0
Release:	%{mkrel 1}
Summary:	Metapackage for synchronizing with Nokia phones
Group:		Communications
License:	GPLv2+
Requires:	libopensync-plugin-gnokii
Requires:	libopensync-plugin-syncml
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package for connecting with Nokia phones. It
depends on all packages necessary for synchronizing with Nokia phones
using the OpenSync framework, via either SyncML or the GNokii
library. It is recommended that you do not install this package
directly, but rather that you install task-nokiasync-gnome or
task-nokiasync-kde, depending on your preferred desktop environment.

%package -n task-nokiasync-kde
Summary:	KDE metapackage for synchronizing with Nokia phones
Group:		Communications
Requires:	task-nokiasync-common
Requires:	libopensync-plugin-kdepim
Requires:	kdepim-kitchensync

%description -n task-nokiasync-kde
This package is a meta-package for connecting with Nokia phones. It
depends on all packages necessary for synchronizing with Nokia phones
using the OpenSync framework, via either SyncML or the GNokii
library, and packages that are useful for synchronizing with KDE
applications.

%package -n task-nokiasync-gnome
Summary:	GNOME metapackage for synchronizing with Nokia phones
Group:		Communications
Requires:	task-nokiasync-common
Requires:	libopensync-plugin-evolution2
Requires:	multisync-gui

%description -n task-nokiasync-gnome
This package is a meta-package for connecting with Nokia phones. It
depends on all packages necessary for synchronizing with Nokia phones
using the OpenSync framework, via either SyncML or the GNokii
library, and packages that are useful for synchronizing with GNOME
applications.

%files

%files -n task-nokiasync-kde

%files -n task-nokiasync-gnome

