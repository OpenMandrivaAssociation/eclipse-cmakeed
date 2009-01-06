%define eclipse_base   %{_libdir}/eclipse
%define install_loc    %{_datadir}/eclipse/dropins/cmakeed

Name:           eclipse-cmakeed
Version:        1.1.0
Release:        %mkrel 0.1.0
Summary:        CMake Editor plug-in for Eclipse

Group:          Development/Java
License:        CPL
URL:            http://cmakeed.sourceforge.net
Source0:        http://heanet.dl.sourceforge.net/sourceforge/cmakeed/CMakeEd-Src-1.1.0.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

BuildRequires: eclipse-pde >= 1:3.4.0
Requires: eclipse-platform >= 3.4.0

%description
The CMakeEd plug-in provides an editor for CMake files. The plug-in
registers an editor for files named CMakeLists.txt and *.cmake.

%prep
%setup -q -c

%build
%{eclipse_base}/buildscripts/pdebuild -a "-DjavacSource=1.5 -DjavacTarget=1.5"

%install
%{__rm} -rf %{buildroot}
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}

%{__unzip} -q -d $RPM_BUILD_ROOT%{install_loc} \
     build/rpmBuild/com.cthing.cmakeed.feature.zip

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{install_loc}
