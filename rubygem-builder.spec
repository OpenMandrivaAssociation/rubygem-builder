%define oname builder

Summary:    Builders for MarkUp
Name:       rubygem-%{oname}
Version:    3.0.0
Release:    %mkrel 1
Group:      Development/Ruby
License:    MIT
URL:        http://builder.rubyforge.org
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
Builder provides a number of builder objects that make creating structured
data simple to do.  Currently the following builder objects are supported:  *
XML Markup * XML Events

%prep

%build

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --no-ri %{SOURCE0}

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib
%{ruby_gemdir}/gems/%{oname}-%{version}/test
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CHANGES
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/doc/releases/builder-1.2.4.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/doc/releases/builder-2.0.0.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/doc/releases/builder-2.1.1.rdoc
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
