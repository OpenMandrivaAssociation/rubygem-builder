# Generated from builder-3.0.0.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	builder

Summary:	Builders for MarkUp
Name:		rubygem-%{rbname}

Version:	3.2.2
Release:	1
Group:		Development/Ruby
License:	MIT
URL:		http://onestepback.org
Source0:	http://rubygems.org/gems/builder-3.2.2.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Builder provides a number of builder objects that make creating structured
data
simple to do.  Currently the following builder objects are supported:
* XML Markup
* XML Events

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f test

%install
%gem_install

%clean

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/builder
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/builder/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/CHANGES
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/README
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/Rakefile
#%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/TAGS
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/doc
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/doc/releases
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/doc/releases/*.rdoc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
