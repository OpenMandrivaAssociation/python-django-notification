%define realname django-notification

Name:           python-django-notification
Version:        1.1.1
Release:        2
Summary:        User notification management for the Django web framework


Group:          Development/Python
License:        MIT
URL:            http://code.google.com/p/django-notification/
Source0:        http://pypi.python.org/packages/source/d/django-notification/django-notification-%{version}.tar.gz

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
python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}

%clean

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE  docs/
%{py_puresitedir}/*



