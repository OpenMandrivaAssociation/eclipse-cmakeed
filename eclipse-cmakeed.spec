%global eclipse_base   %{_libdir}/eclipse
%global install_loc    %{_datadir}/eclipse/dropins/cmakeed

Name:           eclipse-cmakeed
Version:        1.1.5
Release:        4
Summary:        CMake Editor plug-in for Eclipse

Group:          Development/Java
License:        CPL
URL:            https://cmakeed.sourceforge.net
Source0:        http://heanet.dl.sourceforge.net/sourceforge/cmakeed/CMakeEd-Src_%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

BuildRequires: eclipse-pde >= 0:3.4.0
Requires: eclipse-platform >= 3.4.0

%description
The CMakeEd plug-in provides an editor for CMake files. The plug-in registers
an editor for files named CMakeLists.txt and *.cmake.

%prep
%setup -q -n 1_1_5
#remove jar files
find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;

%build
%{eclipse_base}/buildscripts/pdebuild

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m 755 %{buildroot}%{install_loc}

%{__unzip} -q -d %{buildroot}%{install_loc} \
     build/rpmBuild/com.cthing.cmakeed.feature.zip

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{install_loc}
%doc com.cthing.cmakeed.feature/License.html

