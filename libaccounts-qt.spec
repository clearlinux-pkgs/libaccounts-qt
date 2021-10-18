#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libaccounts-qt
Version  : ersion.1.16
Release  : 3
URL      : https://gitlab.com/accounts-sso/libaccounts-qt/-/archive/VERSION_1.16/libaccounts-qt-VERSION_1.16.tar.gz
Source0  : https://gitlab.com/accounts-sso/libaccounts-qt/-/archive/VERSION_1.16/libaccounts-qt-VERSION_1.16.tar.gz
Summary  : Accounts Library
Group    : Development/Tools
License  : LGPL-2.1
Requires: libaccounts-qt-bin = %{version}-%{release}
Requires: libaccounts-qt-lib = %{version}-%{release}
Requires: libaccounts-qt-license = %{version}-%{release}
BuildRequires : buildreq-qmake
BuildRequires : doxygen
BuildRequires : glib-dev
BuildRequires : graphviz
BuildRequires : libaccounts-glib
BuildRequires : libaccounts-glib-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Xml)
BuildRequires : qttools-dev
Patch1: libdir.patch

%description
Accounts management library for Qt applications
=================================================

%package bin
Summary: bin components for the libaccounts-qt package.
Group: Binaries
Requires: libaccounts-qt-license = %{version}-%{release}

%description bin
bin components for the libaccounts-qt package.


%package dev
Summary: dev components for the libaccounts-qt package.
Group: Development
Requires: libaccounts-qt-lib = %{version}-%{release}
Requires: libaccounts-qt-bin = %{version}-%{release}
Provides: libaccounts-qt-devel = %{version}-%{release}
Requires: libaccounts-qt = %{version}-%{release}

%description dev
dev components for the libaccounts-qt package.


%package doc
Summary: doc components for the libaccounts-qt package.
Group: Documentation

%description doc
doc components for the libaccounts-qt package.


%package lib
Summary: lib components for the libaccounts-qt package.
Group: Libraries
Requires: libaccounts-qt-license = %{version}-%{release}

%description lib
lib components for the libaccounts-qt package.


%package license
Summary: license components for the libaccounts-qt package.
Group: Default

%description license
license components for the libaccounts-qt package.


%prep
%setup -q -n libaccounts-qt-VERSION_1.16
cd %{_builddir}/libaccounts-qt-VERSION_1.16
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake -config ltcg -config fat-static-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1634571628
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libaccounts-qt
cp %{_builddir}/libaccounts-qt-VERSION_1.16/COPYING %{buildroot}/usr/share/package-licenses/libaccounts-qt/4df5d4b947cf4e63e675729dd3f168ba844483c7
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/accountstest

%files dev
%defattr(-,root,root,-)
/usr/include/accounts-qt5/Accounts/Account
/usr/include/accounts-qt5/Accounts/AccountService
/usr/include/accounts-qt5/Accounts/Application
/usr/include/accounts-qt5/Accounts/AuthData
/usr/include/accounts-qt5/Accounts/Error
/usr/include/accounts-qt5/Accounts/Manager
/usr/include/accounts-qt5/Accounts/Provider
/usr/include/accounts-qt5/Accounts/Service
/usr/include/accounts-qt5/Accounts/ServiceType
/usr/include/accounts-qt5/Accounts/account-service.h
/usr/include/accounts-qt5/Accounts/account.h
/usr/include/accounts-qt5/Accounts/accountscommon.h
/usr/include/accounts-qt5/Accounts/application.h
/usr/include/accounts-qt5/Accounts/auth-data.h
/usr/include/accounts-qt5/Accounts/error.h
/usr/include/accounts-qt5/Accounts/manager.h
/usr/include/accounts-qt5/Accounts/manager_p.h
/usr/include/accounts-qt5/Accounts/provider.h
/usr/include/accounts-qt5/Accounts/service-type.h
/usr/include/accounts-qt5/Accounts/service.h
/usr/include/accounts-qt5/Accounts/utils.h
/usr/lib64/cmake/AccountsQt5/AccountsQt5Config.cmake
/usr/lib64/cmake/AccountsQt5/AccountsQt5ConfigVersion.cmake
/usr/lib64/libaccounts-qt5.so
/usr/lib64/pkgconfig/accounts-qt5.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/accounts-qt/html/account-service_8cpp_source.html
/usr/share/doc/accounts-qt/html/account-service_8h_source.html
/usr/share/doc/accounts-qt/html/account_8cpp_source.html
/usr/share/doc/accounts-qt/html/account_8h_source.html
/usr/share/doc/accounts-qt/html/accountscommon_8h_source.html
/usr/share/doc/accounts-qt/html/annotated.html
/usr/share/doc/accounts-qt/html/annotated_dup.js
/usr/share/doc/accounts-qt/html/application_8cpp_source.html
/usr/share/doc/accounts-qt/html/application_8h_source.html
/usr/share/doc/accounts-qt/html/auth-data_8cpp_source.html
/usr/share/doc/accounts-qt/html/auth-data_8h_source.html
/usr/share/doc/accounts-qt/html/bc_s.png
/usr/share/doc/accounts-qt/html/bdwn.png
/usr/share/doc/accounts-qt/html/classAccounts_1_1AccountService-members.html
/usr/share/doc/accounts-qt/html/classAccounts_1_1AccountService.html
/usr/share/doc/accounts-qt/html/classAccounts_1_1AccountService.js
/usr/share/doc/accounts-qt/html/classAccounts_1_1Application-members.html
/usr/share/doc/accounts-qt/html/classAccounts_1_1Application.html
/usr/share/doc/accounts-qt/html/classAccounts_1_1Application.js
/usr/share/doc/accounts-qt/html/classAccounts_1_1AuthData-members.html
/usr/share/doc/accounts-qt/html/classAccounts_1_1AuthData.html
/usr/share/doc/accounts-qt/html/classAccounts_1_1AuthData.js
/usr/share/doc/accounts-qt/html/classAccounts_1_1Error-members.html
/usr/share/doc/accounts-qt/html/classAccounts_1_1Error.html
/usr/share/doc/accounts-qt/html/classAccounts_1_1Error.js
/usr/share/doc/accounts-qt/html/classAccounts_1_1Manager-members.html
/usr/share/doc/accounts-qt/html/classAccounts_1_1Manager.html
/usr/share/doc/accounts-qt/html/classAccounts_1_1Manager.js
/usr/share/doc/accounts-qt/html/classAccounts_1_1Provider-members.html
/usr/share/doc/accounts-qt/html/classAccounts_1_1Provider.html
/usr/share/doc/accounts-qt/html/classAccounts_1_1Provider.js
/usr/share/doc/accounts-qt/html/classAccounts_1_1Service-members.html
/usr/share/doc/accounts-qt/html/classAccounts_1_1Service.html
/usr/share/doc/accounts-qt/html/classAccounts_1_1Service.js
/usr/share/doc/accounts-qt/html/classAccounts_1_1ServiceType-members.html
/usr/share/doc/accounts-qt/html/classAccounts_1_1ServiceType.html
/usr/share/doc/accounts-qt/html/classAccounts_1_1ServiceType.js
/usr/share/doc/accounts-qt/html/classes.html
/usr/share/doc/accounts-qt/html/closed.png
/usr/share/doc/accounts-qt/html/deprecated.html
/usr/share/doc/accounts-qt/html/dir_61c9e5842729cb34568d93cb98ad85b9.html
/usr/share/doc/accounts-qt/html/dir_c3d1d086c816c0518443c9e800634b9c.html
/usr/share/doc/accounts-qt/html/dir_c3d1d086c816c0518443c9e800634b9c.js
/usr/share/doc/accounts-qt/html/dir_e68e8157741866f444e17edd764ebbae.html
/usr/share/doc/accounts-qt/html/doc.png
/usr/share/doc/accounts-qt/html/doxygen.css
/usr/share/doc/accounts-qt/html/doxygen.svg
/usr/share/doc/accounts-qt/html/dynsections.js
/usr/share/doc/accounts-qt/html/error_8cpp_source.html
/usr/share/doc/accounts-qt/html/error_8h_source.html
/usr/share/doc/accounts-qt/html/files.html
/usr/share/doc/accounts-qt/html/files_dup.js
/usr/share/doc/accounts-qt/html/folderclosed.png
/usr/share/doc/accounts-qt/html/folderopen.png
/usr/share/doc/accounts-qt/html/functions.html
/usr/share/doc/accounts-qt/html/functions_enum.html
/usr/share/doc/accounts-qt/html/functions_eval.html
/usr/share/doc/accounts-qt/html/functions_func.html
/usr/share/doc/accounts-qt/html/graph_legend.dot
/usr/share/doc/accounts-qt/html/graph_legend.html
/usr/share/doc/accounts-qt/html/index.html
/usr/share/doc/accounts-qt/html/index.qhp
/usr/share/doc/accounts-qt/html/jquery.js
/usr/share/doc/accounts-qt/html/manager_8cpp_source.html
/usr/share/doc/accounts-qt/html/manager_8h_source.html
/usr/share/doc/accounts-qt/html/manager__p_8h_source.html
/usr/share/doc/accounts-qt/html/menu.js
/usr/share/doc/accounts-qt/html/menudata.js
/usr/share/doc/accounts-qt/html/nav_f.png
/usr/share/doc/accounts-qt/html/nav_g.png
/usr/share/doc/accounts-qt/html/nav_h.png
/usr/share/doc/accounts-qt/html/navtree.css
/usr/share/doc/accounts-qt/html/navtree.js
/usr/share/doc/accounts-qt/html/navtreedata.js
/usr/share/doc/accounts-qt/html/navtreeindex0.js
/usr/share/doc/accounts-qt/html/open.png
/usr/share/doc/accounts-qt/html/pages.html
/usr/share/doc/accounts-qt/html/provider_8cpp_source.html
/usr/share/doc/accounts-qt/html/provider_8h_source.html
/usr/share/doc/accounts-qt/html/resize.js
/usr/share/doc/accounts-qt/html/service-type_8cpp_source.html
/usr/share/doc/accounts-qt/html/service-type_8h_source.html
/usr/share/doc/accounts-qt/html/service_8cpp_source.html
/usr/share/doc/accounts-qt/html/service_8h_source.html
/usr/share/doc/accounts-qt/html/splitbar.png
/usr/share/doc/accounts-qt/html/sync_off.png
/usr/share/doc/accounts-qt/html/sync_on.png
/usr/share/doc/accounts-qt/html/tab_a.png
/usr/share/doc/accounts-qt/html/tab_b.png
/usr/share/doc/accounts-qt/html/tab_h.png
/usr/share/doc/accounts-qt/html/tab_s.png
/usr/share/doc/accounts-qt/html/tabs.css
/usr/share/doc/accounts-qt/html/utils_8cpp_source.html
/usr/share/doc/accounts-qt/html/utils_8h_source.html
/usr/share/doc/accounts-qt/qch/accounts.qch

%files lib
%defattr(-,root,root,-)
/usr/lib64/libaccounts-qt5.so.1
/usr/lib64/libaccounts-qt5.so.1.4
/usr/lib64/libaccounts-qt5.so.1.4.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libaccounts-qt/4df5d4b947cf4e63e675729dd3f168ba844483c7
