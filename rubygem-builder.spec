# Generated from builder-3.0.0.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	builder

Summary:	Builders for MarkUp

Name:		rubygem-%{rbname}

Version:	3.2.2
Release:	4
Group:		Development/Ruby
License:	MIT
URL:		https://onestepback.org
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
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
%dir %{gem_dir}/gems/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/builder
%{gem_dir}/gems/%{rbname}-%{version}/lib/builder/*.rb
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{gem_dir}/gems/%{rbname}-%{version}/MIT-LICENSE
%doc %{gem_dir}/gems/%{rbname}-%{version}/CHANGES
%doc %{gem_dir}/gems/%{rbname}-%{version}/README*
%doc %{gem_dir}/gems/%{rbname}-%{version}/Rakefile
#%doc %{gem_dir}/gems/%{rbname}-%{version}/TAGS
%dir %{gem_dir}/gems/%{rbname}-%{version}/test
%{gem_dir}/gems/%{rbname}-%{version}/test/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/doc
%dir %{gem_dir}/gems/%{rbname}-%{version}/doc/releases
%doc %{gem_dir}/gems/%{rbname}-%{version}/doc/releases/*.rdoc
%doc %{gem_dir}/doc/%{rbname}-%{version}


