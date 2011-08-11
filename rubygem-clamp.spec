# Generated from clamp-0.2.3.gem by gem2rpm -*- rpm-spec -*-
%define gemname clamp

%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}
%define rubyabi 1.8

Summary: a minimal framework for command-line utilities
Name: rubygem-%{gemname}
Version: 0.2.3
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/mdub/clamp
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Clamp provides an object-model for command-line utilities.  
It handles parsing of command-line options, and generation of usage help.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
gem install --local --install-dir .%{gemdir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* \
        %{buildroot}%{gemdir}/


%files
%{geminstdir}/
%{geminstdir}/lib
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}


%changelog
* Thu Aug 11 2011 Sergio Rubio <rubiojr@frameos.org> - 0.2.3-2
- fix RHEL5 build

* Thu Aug 11 2011 Sergio Rubio <rubiojr@frameos.org> - 0.2.3-1
- Initial package
