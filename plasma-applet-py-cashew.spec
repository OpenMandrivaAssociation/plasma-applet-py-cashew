%define pname py-cashew

Name:		plasma-applet-py-cashew
Version:	1.1
Release:	6
Summary:	A KDE4 plasmoid that hides the desktop toolbox, also known as the Cashew
Group:		Graphical desktop/KDE
License:	GPLv3+
Url:		http://kde-look.org/content/show.php/Py-Cashew?content=147892
Source0:	%{name}.tar.bz2
BuildRequires:	fdupes
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	zip

Requires:	kdebase4-workspace
Requires:	python-kde4
BuildArch:	noarch

%description
Py-Cashew is a KDE4 plasmoid that hides the desktop toolbox, 
also known as the cashew. Some find the cashew pretty but others
who don't have no way to remove it. The KDE developers made it 
clear that they won't add an option to hide it so this plasmoid 
offers a way out.

%prep
%setup -q

%build
%make

%install
mkdir -p %{buildroot}%{_kde_appsdir}/plasma/plasmoids/%{pname}
cp -r contents py-cashew.png metadata.desktop %{buildroot}%{_kde_appsdir}/plasma/plasmoids/%{pname}/

mkdir -p %{buildroot}%{_kde_services}
cp metadata.desktop %{buildroot}%{_kde_services}/plasma-applet-%{pname}.desktop

%files
%doc COPYING README
%{_kde_appsdir}/plasma/plasmoids/%{pname}/*
%{_kde_services}/plasma-applet-%{pname}.desktop

