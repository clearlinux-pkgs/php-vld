#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-vld
Version  : 0.18.0
Release  : 30
URL      : https://pecl.php.net/get/vld-0.18.0.tgz
Source0  : https://pecl.php.net/get/vld-0.18.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: php-vld-lib = %{version}-%{release}
Requires: php-vld-license = %{version}-%{release}
BuildRequires : buildreq-php

%description
======
This extension is to show low level PHP structures. It is therefore very
sensitive to changes in the PHP API. If the PECL install doesn't work, please
try the latest version from GitHub::

%package lib
Summary: lib components for the php-vld package.
Group: Libraries
Requires: php-vld-license = %{version}-%{release}

%description lib
lib components for the php-vld package.


%package license
Summary: license components for the php-vld package.
Group: Default

%description license
license components for the php-vld package.


%prep
%setup -q -n vld-0.18.0
cd %{_builddir}/vld-0.18.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-vld
cp %{_builddir}/vld-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-vld/e67db0ccdc7dc6c502aadb0c020212cda347ed39 || :
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/vld.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-vld/e67db0ccdc7dc6c502aadb0c020212cda347ed39
