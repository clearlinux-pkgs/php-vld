#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-vld
Version  : 0.17.2
Release  : 19
URL      : https://pecl.php.net/get/vld-0.17.2.tgz
Source0  : https://pecl.php.net/get/vld-0.17.2.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: php-vld-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
======
This extension is to show low level PHP structures. It is therefore very
sensitive to changes in the PHP API. If the PECL install doesn't work, please
try the latest version from GitHub::

%package lib
Summary: lib components for the php-vld package.
Group: Libraries

%description lib
lib components for the php-vld package.


%prep
%setup -q -n vld-0.17.2
cd %{_builddir}/vld-0.17.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/vld.so
