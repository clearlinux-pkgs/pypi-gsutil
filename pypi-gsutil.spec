#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-gsutil
Version  : 5.20
Release  : 102
URL      : https://files.pythonhosted.org/packages/ca/4c/c5a55275e8c15b58436f5041bf91bbc420372bceabad3969819c88cbfe7c/gsutil-5.20.tar.gz
Source0  : https://files.pythonhosted.org/packages/ca/4c/c5a55275e8c15b58436f5041bf91bbc420372bceabad3969819c88cbfe7c/gsutil-5.20.tar.gz
Summary  : A command line tool for interacting with cloud storage services.
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: pypi-gsutil-bin = %{version}-%{release}
Requires: pypi-gsutil-license = %{version}-%{release}
Requires: pypi-gsutil-python = %{version}-%{release}
Requires: pypi-gsutil-python3 = %{version}-%{release}
Requires: PySocks
BuildRequires : PySocks
BuildRequires : buildreq-distutils3
BuildRequires : pypi(argcomplete)
BuildRequires : pypi(crcmod)
BuildRequires : pypi(fasteners)
BuildRequires : pypi(gcs_oauth2_boto_plugin)
BuildRequires : pypi(google_apitools)
BuildRequires : pypi(google_reauth)
BuildRequires : pypi(httplib2)
BuildRequires : pypi(httpretty)
BuildRequires : pypi(monotonic)
BuildRequires : pypi(paramiko)
BuildRequires : pypi(pyasn1)
BuildRequires : pypi(pyasn1_modules)
BuildRequires : pypi(pyopenssl)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(requests)
BuildRequires : pypi(retry_decorator)
BuildRequires : pypi(rsa)
BuildRequires : pypi(simplejson)
BuildRequires : pypi(six)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This directory contains library code used by gsutil. Users are cautioned not
to write programs that call the internal interfaces defined in here; these
interfaces were defined only for use by gsutil, and are subject to change
without notice. Moreover, Google supports this library only when used by
gsutil, not when the library interfaces are called directly by other programs.

%package bin
Summary: bin components for the pypi-gsutil package.
Group: Binaries
Requires: pypi-gsutil-license = %{version}-%{release}

%description bin
bin components for the pypi-gsutil package.


%package license
Summary: license components for the pypi-gsutil package.
Group: Default

%description license
license components for the pypi-gsutil package.


%package python
Summary: python components for the pypi-gsutil package.
Group: Default
Requires: pypi-gsutil-python3 = %{version}-%{release}

%description python
python components for the pypi-gsutil package.


%package python3
Summary: python3 components for the pypi-gsutil package.
Group: Default
Requires: python3-core
Provides: pypi(gsutil)
Requires: pypi(argcomplete)
Requires: pypi(crcmod)
Requires: pypi(fasteners)
Requires: pypi(gcs_oauth2_boto_plugin)
Requires: pypi(google_apitools)
Requires: pypi(google_auth)
Requires: pypi(google_reauth)
Requires: pypi(httplib2)
Requires: pypi(httpretty)
Requires: pypi(monotonic)
Requires: pypi(paramiko)
Requires: pypi(pyasn1)
Requires: pypi(pyasn1_modules)
Requires: pypi(pyopenssl)
Requires: pypi(pyyaml)
Requires: pypi(requests)
Requires: pypi(retry_decorator)
Requires: pypi(rsa)
Requires: pypi(simplejson)
Requires: pypi(six)

%description python3
python3 components for the pypi-gsutil package.


%prep
%setup -q -n gsutil-5.20
cd %{_builddir}/gsutil-5.20
pushd ..
cp -a gsutil-5.20 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1675377385
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . httplib2
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . httplib2
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-gsutil
cp %{_builddir}/gsutil-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-gsutil/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/gsutil-%{version}/gslib/vendored/boto/LICENSE %{buildroot}/usr/share/package-licenses/pypi-gsutil/875c7866415e9e58a4c515bd052d001ac5107943 || :
cp %{_builddir}/gsutil-%{version}/gslib/vendored/oauth2client/LICENSE %{buildroot}/usr/share/package-licenses/pypi-gsutil/a7b6feb97b476557d3d699fa1f20090fb956d662 || :
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} httplib2
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
## install_append content
sitedir=$(python -c "import sys; print(sys.path[-1])")
rm -rfv %{buildroot}/${sitedir}/test
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gsutil

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-gsutil/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/pypi-gsutil/875c7866415e9e58a4c515bd052d001ac5107943
/usr/share/package-licenses/pypi-gsutil/a7b6feb97b476557d3d699fa1f20090fb956d662

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
