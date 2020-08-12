//
// This macro is an example for generating single particles written in the 
// PHPythia format (which is fun4all compliant)
//
// It is based on macros used in various analyses (e.g. for embedding) but redacted and
// simplified for clarity. As such, it will not be suitable for real applications.
//
// A flat pT distribution is used. A distrubution of the vertex coordinates was used.
// 
// A few additional comments/annotations were added.
//
//
void
phparticlegen_example(const int nevents = 10, int pid=11, const char *outputname = "phparticlegen_example.root")
{
  gSystem->Load("libPythia6.so");
  gSystem->Load("libfun4all.so");	// framework + reco modules
  gSystem->Load("libpdbcalBase.so");
  gSystem->Load("libPHParticleGen.so");
  gSystem->Load("libPHPythia.so");
  gSystem->ListLibraries();

  recoConsts *rc = recoConsts::instance(); // fun4all/PHOOL singleton class
  rc->set_IntFlag("RUNNUMBER",0);

  //  Instantiate a Fun4All Server
  Fun4AllServer *se = Fun4AllServer::instance();

  // A custom generator can be added here
  PHParticleGen* ss = new PHParticleGen();

  // Can optionally set the seed, otherwise defaults to /dev/random
  // ss->SetSeed(1999);

  //*** Set Particle Parameters. Overrides config file.

  // Particle ID
  ss->GetGenerator()->SetParameter("pid", pid);	// e+

  // Momentum/Transverse Momentum/Energy
  ss->GetGenerator()->SetParameter("momflag",TSingleParticleGenerator::FLAT_PT);
  ss->GetGenerator()->SetParameter("pmin",0.5);
  ss->GetGenerator()->SetParameter("pmax",10.);

  // Eta
  ss->GetGenerator()->SetParameter("etamin",-0.5);
  ss->GetGenerator()->SetParameter("etamax", 0.5);

  // steps and phi distribution
  ss->GetGenerator()->SetParameter("nstepse",100.);
  ss->GetGenerator()->SetParameter("nstepstheta",100.);
  ss->GetGenerator()->SetParameter("nstepsphi",100);
  ss->GetGenerator()->SetParameter("phitot",0.5);

  // Vertex Distribution (sometimes better to leave at 0)
  ss->GetGenerator()->SetParameter("vtxflag",TSingleParticleGenerator::FLAT);

  ss->GetGenerator()->SetParameter("xcenter", 0.0);
  ss->GetGenerator()->SetParameter("ycenter", 0.0);
  ss->GetGenerator()->SetParameter("zcenter", 0.0);
  ss->GetGenerator()->SetParameter("xwidth", 0.5);
  ss->GetGenerator()->SetParameter("ywidth", 0.5);
  ss->GetGenerator()->SetParameter("zwidth", 0.5);

  // Register with the Fun4All server:
  se->registerSubsystem(ss);

  // This is to read in null events (necessary for Fun4All Framework)
  Fun4AllDummyInputManager *in1 = new Fun4AllDummyInputManager("DSTin1", "DST");
  se->registerInputManager(in1);

  TString OUTPUT = outputname;
  Fun4AllDstOutputManager *dst_output_mgr  = new Fun4AllDstOutputManager("PHPYTHIA",OUTPUT.Data());
  
  dst_output_mgr->AddNode("Sync");
  dst_output_mgr->AddNode("PHPythiaHeader");
  dst_output_mgr->AddNode("PHPythia");
  
  se->registerOutputManager(dst_output_mgr);

  cout<<" PHParticleGen will generate "<<nevents<<" events"<<endl;

  se->run(nevents);  // run over all events
  se->End();

}

