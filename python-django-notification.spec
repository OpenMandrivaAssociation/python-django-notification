%define realname django-notification

Name:           python-django-notification
Version:        0.1.5
Release:        %mkrel 2
Summary:        User notification management for the Django web framework

Group:          Development/Python
License:        MIT
URL:            http://code.google.com/p/django-notification/
Source0:        http://pypi.python.org/packages/source/d/django-notification/%{realname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires:       python-django

%description
Many sites need to notify users when certain events have occurred and to
allow configurable options as to how those notifications are to be received.

The project aims to provide a Django app for this sort of functionality.
This includes:

    * submission of notification messages by other apps
    * notification messages on signing in
    * notification messages via email (configurable by user)
    * notification messages via feed

%prep
%setup -q -n %{realname}-%{version}
find -name '._*' -exec rm {} \;

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE README docs/
%{py_puresitedir}/*


%changelog
* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.1.5-2mdv2011.0
+ Revision: 592232
- rebuild for python 2.7

* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.5-1mdv2010.1
+ Revision: 489187
- update to new version 0.1.5

* Tue Jun 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.3-1mdv2010.0
+ Revision: 384247
- update to new version 0.1.3

* Fri Mar 06 2009 Jérôme Soyer <saispo@mandriva.org> 0.1.2-1mdv2009.1
+ Revision: 349662
- import python-django-notification


