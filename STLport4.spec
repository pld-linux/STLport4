Summary:	C++ standard library
Summary(pl.UTF-8):	Biblioteki standardowe C++
Name:		STLport4
Version:	4.6.2
Release:	1
License:	distributable (see README.gz)
Group:		Libraries
Source0:	http://www.stlport.com/archive/STLport-%{version}.tar.gz
# Source0-md5:	4c01c84f1212369ceb369567ed06d1a2
Patch0:		%{name}-nodebug.patch
Patch1:		%{name}-soname.patch
Patch2:		%{name}-gcc34.patch
Patch3:		%{name}-4.5.3-gcc3stdexcept.patch
Patch4:		%{name}-4.5.3-extra-cxxflags.patch
URL:		http://www.stlport.org/
BuildRequires:	libstdc++-devel >= 5:3.3.2
%requires_eq	libstdc++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
STLport is a multiplatform implementation of C++ Standard Template
Library based on SGI STL. It's used by e.g. OpenOffice.

%description -l pl.UTF-8
STLport to wieloplatformowa implementacja standardowej biblioteki
szablonów (Standard Template Library) C++ oparta na SGI STL. Jest
używana m.in. przez OpenOffice.

%package devel
Summary:	STLport heades files, documentation
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do STLport
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and development documentation for STLport.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja dla STLport.

%package static
Summary:	Static STLport libraries
Summary(pl.UTF-8):	Biblioteki statyczne do STLport
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static STLport libraries.

%description static -l pl.UTF-8
Biblioteki statyczne do STLport.

%prep
%setup -q -n STLport-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__make} -C src -f gcc.mak \
	CXXFLAGS="%{rpmcxxflags}" \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src -f gcc.mak install \
	INSTALLDIR=$RPM_BUILD_ROOT%{_prefix} \
	INSTALLDIR_LIB=$RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/*.so.*.*
%attr(755,root,root) %{_libdir}/*.so

%files devel
%defattr(644,root,root,755)
%doc doc/{images,README.gcc.html,[a-z]*.html}
%{_includedir}/stlport

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
