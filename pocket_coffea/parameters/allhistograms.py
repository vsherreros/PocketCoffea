# Histograms binning and labeling

from math import pi

histogram_settings = {
    'variables': {
        'muon_pt': {
            'binning': {'n_or_arr': 200, 'lo': 0, 'hi': 2000},
            'xlim': (0, 500),
            'xlabel': "$p_{T}^{\mu}$ [GeV]",
        },
        'muon_eta': {
            'binning': {'n_or_arr': 80, 'lo': -4, 'hi': 4},
            'xlim': (-4, 4),
            'xlabel': "$\eta_{\mu}$",
        },
        'muon_phi': {
            'binning': {'n_or_arr': 128, 'lo': -pi, 'hi': pi},
            'xlim': (-pi, pi),
            'xlabel': "$\phi_{\mu}$",
        },
        'goodmuon_pt': {
            'binning': {'n_or_arr': 200, 'lo': 0, 'hi': 2000},
            'xlim': (0, 500),
            'xlabel': "$p_{T}^{\mu}$ [GeV]",
        },
        'goodmuon_eta': {
            'binning': {'n_or_arr': 80, 'lo': -4, 'hi': 4},
            'xlim': (-4, 4),
            'xlabel': "$\eta_{\mu}$",
        },
        'goodmuon_phi': {
            'binning': {'n_or_arr': 128, 'lo': -pi, 'hi': pi},
            'xlim': (-pi, pi),
            'xlabel': "$\phi_{\mu}$",
        },
        'electron_pt': {
            'binning': {'n_or_arr': 200, 'lo': 0, 'hi': 2000},
            'xlim': (0, 500),
            'xlabel': "$p_{T}^{e}$ [GeV]",
        },
        'electron_eta': {
            'binning': {'n_or_arr': 80, 'lo': -4, 'hi': 4},
            'xlim': (-4, 4),
            'xlabel': "$\eta_{e}$",
        },
        "electron_etaSC": {
            'binning': {
                'n_or_arr': [
                    -2.5,
                    -2.3,
                    -2.1,
                    -1.9,
                    -1.7,
                    -1.5660,
                    -1.4442,
                    -1.2,
                    -1.0,
                    -0.8,
                    -0.6,
                    -0.4,
                    -0.2,
                    0.0,
                    0.2,
                    0.4,
                    0.6,
                    0.8,
                    1.0,
                    1.2,
                    1.4442,
                    1.5660,
                    1.7,
                    1.9,
                    2.1,
                    2.3,
                    2.5,
                ]
            },
            'ylim': (-2.5, 2.5),
            'ylabel': "Electron Supercluster $\eta$",
        },
        'electron_phi': {
            'binning': {'n_or_arr': 128, 'lo': -pi, 'hi': pi},
            'xlim': (-pi, pi),
            'xlabel': "$\phi_{e}$",
        },
        'goodelectron_pt': {
            'binning': {'n_or_arr': 200, 'lo': 0, 'hi': 2000},
            'xlim': (0, 500),
            'xlabel': "$p_{T}^{e}$ [GeV]",
        },
        'goodelectron_eta': {
            'binning': {'n_or_arr': 80, 'lo': -4, 'hi': 4},
            'xlim': (-4, 4),
            'xlabel': "$\eta_{e}$",
        },
        'goodelectron_phi': {
            'binning': {'n_or_arr': 128, 'lo': -pi, 'hi': pi},
            'xlim': (-pi, pi),
            'xlabel': "$\phi_{e}$",
        },
        'jet_pt': {
            'binning': {'n_or_arr': 150, 'lo': 0, 'hi': 1500},
            'xlim': (0, 500),
            'xlabel': "$p_{T}^{j}$ [GeV]",
        },
        'jet_eta': {
            'binning': {'n_or_arr': 80, 'lo': -4, 'hi': 4},
            'xlim': (-4, 4),
            'xlabel': "$\eta_{j}$",
        },
        'jet_phi': {
            'binning': {'n_or_arr': 128, 'lo': -pi, 'hi': pi},
            'xlim': (-pi, pi),
            'xlabel': "$\phi_{j}$",
        },
        'jet_btagDeepFlavB': {
            'binning': {'n_or_arr': 50, 'lo': 0, 'hi': 1},
            'xlim': (0, 1),
            'xlabel': "AK4 DeepJet b-tag score",
        },
        'goodjet_pt': {
            'binning': {'n_or_arr': 150, 'lo': 0, 'hi': 1500},
            'xlim': (0, 500),
            'xlabel': "$p_{T}^{j}$ [GeV]",
        },
        'goodjet_eta': {
            'binning': {'n_or_arr': 80, 'lo': -4, 'hi': 4},
            'xlim': (-4, 4),
            'xlabel': "$\eta_{j}$",
        },
        'goodjet_phi': {
            'binning': {'n_or_arr': 128, 'lo': -pi, 'hi': pi},
            'xlim': (-pi, pi),
            'xlabel': "$\phi_{j}$",
        },
        'nmuon': {
            'binning': {'n_or_arr': 5, 'lo': 0, 'hi': 5},
            'xlim': (0, 5),
            'xlabel': "$N_{\mu}$",
        },
        'nelectron': {
            'binning': {'n_or_arr': 5, 'lo': 0, 'hi': 5},
            'xlim': (0, 5),
            'xlabel': "$N_{e}$",
        },
        'nlep': {
            'binning': {'n_or_arr': 5, 'lo': 0, 'hi': 5},
            'xlim': (0, 5),
            'xlabel': "$N_{lep}$",
        },
        'njet': {
            'binning': {'n_or_arr': 25, 'lo': 0, 'hi': 25},
            'xlim': (0, 25),
            'xlabel': "$N_{jet}$",
        },
        'ht': {
            'binning': {'n_or_arr': 400, 'lo': 0, 'hi': 4000},
            'xlim': (0, 1000),
            'xlabel': "$H_T$",
        },
        'nmuongood': {
            'binning': {'n_or_arr': 5, 'lo': 0, 'hi': 5},
            'xlim': (0, 5),
            'xlabel': "$N_{\mu}$",
        },
        'nelectrongood': {
            'binning': {'n_or_arr': 5, 'lo': 0, 'hi': 5},
            'xlim': (0, 5),
            'xlabel': "$N_{e}$",
        },
        'ngoodjet': {
            'binning': {'n_or_arr': 25, 'lo': 0, 'hi': 25},
            'xlim': (0, 25),
            'xlabel': "$N_{goodjet}$",
        },
        'nlepgood': {
            'binning': {'n_or_arr': 5, 'lo': 0, 'hi': 5},
            'xlim': (0, 5),
            'xlabel': "$N_{lep}$",
        },
        'nbjet': {
            'binning': {'n_or_arr': 20, 'lo': 0, 'hi': 20},
            'xlim': (0, 20),
            'xlabel': "$N_{b-jet}$",
        },
        'nparton': {
            'binning': {'n_or_arr': 20, 'lo': 0, 'hi': 20},
            'xlim': (0, 20),
            'xlabel': "$N_{parton}$",
        },
        'nparton_matched': {
            'binning': {'n_or_arr': 20, 'lo': 0, 'hi': 20},
            'xlim': (0, 20),
            'xlabel': "$N_{parton,matched}$",
        },
        'nfatjet': {
            'binning': {'n_or_arr': 10, 'lo': 0, 'hi': 10},
            'xlim': (0, 10),
            'xlabel': "$N_{fatjet}$",
        },
        'parton_pt': {
            'binning': {'n_or_arr': 150, 'lo': 0, 'hi': 1500},
            'xlim': (0, 500),
            'xlabel': "$p_{T}^{parton}$ [GeV]",
        },
        'parton_eta': {
            'binning': {'n_or_arr': 80, 'lo': -4, 'hi': 4},
            'xlim': (-4, 4),
            'xlabel': "$\eta_{parton}$",
        },
        'parton_phi': {
            'binning': {'n_or_arr': 128, 'lo': -pi, 'hi': pi},
            'xlim': (-pi, pi),
            'xlabel': "$\phi_{parton}$",
        },
        'parton_dRMatchedJet': {
            'binning': {'n_or_arr': 200, 'lo': 0, 'hi': 5},
            'xlim': (0, 1),
            'xlabel': r'min ${\Delta}R_{parton,jet}$',
        },
        'parton_pdgId': {
            'binning': {'n_or_arr': 50, 'lo': -25, 'hi': 25},
            'xlim': (0, 1),
            'xlabel': r'Parton pdgId',
        },
        'charge_sum': {
            'binning': {'n_or_arr': 12, 'lo': -6, 'hi': 6},
            'xlim': (-6, 6),
            'xlabel': "lepton charge sum",
        },
        'met_pt': {
            'binning': {'n_or_arr': 200, 'lo': 0, 'hi': 2000},
            'xlim': (0, 500),
            'xlabel': "$p_{T}^{MET}$ [GeV]",
        },
        'met_phi': {
            'binning': {'n_or_arr': 128, 'lo': -pi, 'hi': pi},
            'xlim': (-pi, pi),
            'xlabel': "$\phi_{MET}$",
        },
        'mll': {
            'binning': {'n_or_arr': 300, 'lo': 0, 'hi': 1500},
            'xlim': (0, 500),
            'xlabel': "$m_{\ell\ell}$ [GeV]",
        },
        'leading_jet_pt': {
            'binning': {'n_or_arr': 150, 'lo': 0, 'hi': 1500},
            'xlim': (0, 500),
            'xlabel': "$p_{T}^{j,1}$ [GeV]",
        },
        'leading_jet_eta': {
            'binning': {'n_or_arr': 80, 'lo': -4, 'hi': 4},
            'xlim': (-4, 4),
            'xlabel': "$\eta_{j,1}$ [GeV]",
        },
        'leading_jet_phi': {
            'binning': {'n_or_arr': 128, 'lo': -pi, 'hi': pi},
            'xlim': (-pi, pi),
            'xlabel': "$\phi_{j,1}$",
        },
        'leading_jet_mass': {
            'binning': {'n_or_arr': 300, 'lo': 0, 'hi': 300},
            'xlim': (0, 300),
            'xlabel': "$m_{j,1}$ [GeV]",
        },
        'leading_bjet_pt': {
            'binning': {'n_or_arr': 150, 'lo': 0, 'hi': 1500},
            'xlim': (0, 500),
            'xlabel': "$p_{T}^{b,1}$ [GeV]",
        },
        'leading_bjet_eta': {
            'binning': {'n_or_arr': 80, 'lo': -4, 'hi': 4},
            'xlim': (-4, 4),
            'xlabel': "$\eta_{b,1}$ [GeV]",
        },
        'leading_bjet_phi': {
            'binning': {'n_or_arr': 128, 'lo': -pi, 'hi': pi},
            'xlim': (-pi, pi),
            'xlabel': "$\phi_{b,1}$",
        },
        'leading_bjet_mass': {
            'binning': {'n_or_arr': 300, 'lo': 0, 'hi': 300},
            'xlim': (0, 300),
            'xlabel': "$m_{b,1}$ [GeV]",
        },
        'leadAK8JetMass': {
            'binning': {'n_or_arr': 300, 'lo': 0, 'hi': 300},
            'xlim': (0, 300),
            'xlabel': "FatJet $m_{SD}$",
        },
        'leadAK8JetPt': {
            'binning': {'n_or_arr': 500, 'lo': 0, 'hi': 5000},
            'xlim': (0, 1000),
            'xlabel': "FatJet $p_T$",
        },
        'leadAK8JetEta': {
            'binning': {'n_or_arr': 80, 'lo': -4, 'hi': 4},
            'xlim': (-4, 4),
            'xlabel': "FatJet $\eta$",
        },
        'leadAK8JetPhi': {
            'binning': {'n_or_arr': 128, 'lo': -pi, 'hi': pi},
            'xlim': (-pi, pi),
            'xlabel': "FatJet $\phi$",
        },
        'leadAK8JetRho': {
            'binning': {'n_or_arr': 800, 'lo': -8, 'hi': 0},
            'xlim': (-7, 0),
            'xlabel': r'FatJet $\rho$',
        },
        'leadAK8JetHbb': {
            'binning': {'n_or_arr': 50, 'lo': 0, 'hi': 1},
            'xlim': (0, 1),
            'xlabel': r'btagDDBvL',
        },
        'leadAK8JetTau21': {
            'binning': {'n_or_arr': 40, 'lo': 0, 'hi': 1},
            'xlim': (0, 1),
            'xlabel': r'FatJet $\tau_{21}$',
        },
        'lepton_plus_pt': {
            'binning': {'n_or_arr': 200, 'lo': 0, 'hi': 2000},
            'xlim': (0, 500),
            'xlabel': "$p_{T}^{\ell^+}$ [GeV]",
        },
        'lepton_plus_eta': {
            'binning': {'n_or_arr': 80, 'lo': -4, 'hi': 4},
            'xlim': (-4, 4),
            'xlabel': "$\eta_{\ell^+}$",
        },
        'lepton_plus_phi': {
            'binning': {'n_or_arr': 128, 'lo': -pi, 'hi': pi},
            'xlim': (-pi, pi),
            'xlabel': "$\phi_{\ell^+}$",
        },
        'lepton_plus_mass': {
            'binning': {'n_or_arr': 300, 'lo': 0, 'hi': 300},
            'xlim': (0, 300),
            'xlabel': "$m_{\ell^+}$ [GeV]",
        },
        'lepton_minus_pt': {
            'binning': {'n_or_arr': 200, 'lo': 0, 'hi': 2000},
            'xlim': (0, 500),
            'xlabel': "$p_{T}^{\ell^-}$ [GeV]",
        },
        'lepton_minus_eta': {
            'binning': {'n_or_arr': 80, 'lo': -4, 'hi': 4},
            'xlim': (-4, 4),
            'xlabel': "$\eta_{\ell^-}$",
        },
        'lepton_minus_phi': {
            'binning': {'n_or_arr': 128, 'lo': -pi, 'hi': pi},
            'xlim': (-pi, pi),
            'xlabel': "$\phi_{\ell^-}$",
        },
        'lepton_minus_mass': {
            'binning': {'n_or_arr': 300, 'lo': 0, 'hi': 300},
            'xlim': (0, 300),
            'xlabel': "$m_{\ell^-}$ [GeV]",
        },
        'leading_lepton_pt': {
            'binning': {'n_or_arr': 200, 'lo': 0, 'hi': 2000},
            'xlim': (0, 500),
            'xlabel': "$p_{T}^{\ell,1}$ [GeV]",
        },
        'leading_lepton_eta': {
            'binning': {'n_or_arr': 80, 'lo': -4, 'hi': 4},
            'xlim': (-4, 4),
            'xlabel': "$\eta_{\ell,1}$",
        },
        'leading_lepton_phi': {
            'binning': {'n_or_arr': 128, 'lo': -pi, 'hi': pi},
            'xlim': (-pi, pi),
            'xlabel': "$\phi_{\ell,1}$",
        },
        'leading_lepton_mass': {
            'binning': {'n_or_arr': 300, 'lo': 0, 'hi': 300},
            'xlim': (0, 300),
            'xlabel': "$m_{\ell,1}$ [GeV]",
        },
        'ptll': {
            'binning': {'n_or_arr': 400, 'lo': 0, 'hi': 2000},
            'xlim': (0, 500),
            'xlabel': "$p_{T}^{\ell\ell}$ [GeV]",
        },
        'mt_ww': {
            'binning': {'n_or_arr': 400, 'lo': 0, 'hi': 2000},
            'xlim': (0, 500),
            'xlabel': "$m_{T}^{WW}$ [GeV]",
        },
        'pnu_x': {
            'binning': {'n_or_arr': 200, 'lo': -1000, 'hi': 1000},
            'xlim': (-300, 300),
            'xlabel': r'$p_{\nu_x}$ [GeV]',
        },
        'pnu_y': {
            'binning': {'n_or_arr': 200, 'lo': -1000, 'hi': 1000},
            'xlim': (-300, 300),
            'xlabel': r'$p_{\nu_y}$ [GeV]',
        },
        'pnu_z': {
            'binning': {'n_or_arr': 200, 'lo': -1000, 'hi': 1000},
            'xlim': (-300, 300),
            'xlabel': r'$p_{\nu_z}$ [GeV]',
        },
        'pnubar_x': {
            'binning': {'n_or_arr': 200, 'lo': -1000, 'hi': 1000},
            'xlim': (-300, 300),
            'xlabel': r'$p_{\bar{\nu}_x}$ [GeV]',
        },
        'pnubar_y': {
            'binning': {'n_or_arr': 200, 'lo': -1000, 'hi': 1000},
            'xlim': (-300, 300),
            'xlabel': r'$p_{\bar{\nu}_y}$ [GeV]',
        },
        'pnubar_z': {
            'binning': {'n_or_arr': 200, 'lo': -1000, 'hi': 1000},
            'xlim': (-300, 300),
            'xlabel': r'$p_{\bar{\nu}_z}$ [GeV]',
        },
        'm_w_plus': {
            'binning': {'n_or_arr': 300, 'lo': 0, 'hi': 1500},
            'xlim': (0, 500),
            'xlabel': "$m_{W^+}$ [GeV]",
        },
        'm_w_minus': {
            'binning': {'n_or_arr': 300, 'lo': 0, 'hi': 1500},
            'xlim': (0, 500),
            'xlabel': "$m_{W^-}$ [GeV]",
        },
        'm_top': {
            'binning': {'n_or_arr': 400, 'lo': 0, 'hi': 2000},
            'xlim': (0, 500),
            'xlabel': "$m_{t}$ [GeV]",
        },
        'm_topbar': {
            'binning': {'n_or_arr': 400, 'lo': 0, 'hi': 2000},
            'xlim': (0, 500),
            'xlabel': r'$m_{\bar{t}}$ [GeV]',
        },
        'm_tt': {
            'binning': {'n_or_arr': 300, 'lo': 0, 'hi': 3000},
            'xlim': (0, 2000),
            'xlabel': r'$m_{t\bar{t}}$ [GeV]',
        },
        'tt_pt': {
            'binning': {'n_or_arr': 200, 'lo': 0, 'hi': 2000},
            'xlim': (0, 1000),
            'xlabel': r'$p_{T}^{t\bar{t}}$ [GeV]',
        },
        'top_pt': {
            'binning': {'n_or_arr': 200, 'lo': 0, 'hi': 2000},
            'xlim': (0, 1000),
            'xlabel': r'$p_{T}^{t}$ [GeV]',
        },
        'topbar_pt': {
            'binning': {'n_or_arr': 200, 'lo': 0, 'hi': 2000},
            'xlim': (0, 1000),
            'xlabel': r'$p_{T}^{\bar{t}}$ [GeV]',
        },
        'nNu': {
            'binning': {'n_or_arr': 5, 'lo': 0, 'hi': 5},
            'xlim': (0, 5),
            'xlabel': "$N_{\nu_{reco}}$",
        },
        'nNubar': {
            'binning': {'n_or_arr': 5, 'lo': 0, 'hi': 5},
            'xlim': (0, 5),
            'xlabel': "$N_{\bar{\nu}_{reco}}$",
        },
        'nNuGen': {
            'binning': {'n_or_arr': 5, 'lo': 0, 'hi': 5},
            'xlim': (0, 5),
            'xlabel': "$N_{\nu_{gen}}$",
        },
        'nNubarGen': {
            'binning': {'n_or_arr': 5, 'lo': 0, 'hi': 5},
            'xlim': (0, 5),
            'xlabel': "$N_{\bar{\nu}_{gen}}$",
        },
        'ratioNuPtGenReco': {
            'binning': {'n_or_arr': 100, 'lo': -5, 'hi': 5},
            'xlim': (-5, 5),
            'xlabel': r'$p_{T}^{\nu_{gen}} / p_{T}^{\nu_{reco}}$ [GeV]',
        },
        'ratioNubarPtGenReco': {
            'binning': {'n_or_arr': 100, 'lo': -5, 'hi': 5},
            'xlim': (-5, 5),
            'xlabel': r'$p_{T}^{\bar{\nu}_{gen}} / p_{T}^{\bar{\nu}_{reco}}$ [GeV]',
        },
        'deltaRNuNuGen': {
            'binning': {'n_or_arr': 64, 'lo': 0, 'hi': 5},
            'xlim': (0, 5),
            'xlabel': r'${\Delta}R_{\nu_{reco},\nu_{gen}}$',
        },
        'deltaRNubarNubarGen': {
            'binning': {'n_or_arr': 64, 'lo': 0, 'hi': 5},
            'xlim': (0, 5),
            'xlabel': r'${\Delta}R_{\bar{\nu}_{reco},\bar{\nu}_{gen}}$',
        },
        'deltaRLeptonPlusHiggs': {
            'binning': {'n_or_arr': 64, 'lo': 0, 'hi': 5},
            'xlim': (0, 5),
            'xlabel': r'${\Delta}R_{H,\ell^+$',
        },
        'deltaRLeptonMinusHiggs': {
            'binning': {'n_or_arr': 64, 'lo': 0, 'hi': 5},
            'xlim': (0, 5),
            'xlabel': r'${\Delta}R_{H,\ell^-$',
        },
        'deltaRBBbar': {
            'binning': {'n_or_arr': 64, 'lo': 0, 'hi': 5},
            'xlim': (0, 5),
            'xlabel': r'${\Delta}R_{b,\bar{b}}$',
        },
        'deltaRHiggsTop': {
            'binning': {'n_or_arr': 64, 'lo': 0, 'hi': 5},
            'xlim': (0, 5),
            'xlabel': r'${\Delta}R_{H,t}$',
        },
        'deltaRHiggsTopbar': {
            'binning': {'n_or_arr': 64, 'lo': 0, 'hi': 5},
            'xlim': (0, 5),
            'xlabel': r'${\Delta}R_{H,\bar{t}}$',
        },
        'deltaRHiggsTT': {
            'binning': {'n_or_arr': 64, 'lo': 0, 'hi': 5},
            'xlim': (0, 5),
            'xlabel': r'${\Delta}R_{H,t\bar{t}}$',
        },
        'deltaRTopTopbar': {
            'binning': {'n_or_arr': 64, 'lo': 0, 'hi': 5},
            'xlim': (0, 5),
            'xlabel': r'${\Delta}R_{t,\bar{t}}$',
        },
        'deltaPhiBBbar': {
            'binning': {'n_or_arr': 64, 'lo': 0, 'hi': pi},
            'xlim': (0, pi),
            'xlabel': r'${\Delta}\phi_{b,\bar{b}}$',
        },
        'deltaPhiHiggsTop': {
            'binning': {'n_or_arr': 64, 'lo': 0, 'hi': pi},
            'xlim': (0, pi),
            'xlabel': r'${\Delta}\phi_{H,t}$',
        },
        'deltaPhiHiggsTopbar': {
            'binning': {'n_or_arr': 64, 'lo': 0, 'hi': pi},
            'xlim': (0, pi),
            'xlabel': r'${\Delta}\phi_{H,\bar{t}}$',
        },
        'deltaPhiHiggsTT': {
            'binning': {'n_or_arr': 64, 'lo': 0, 'hi': pi},
            'xlim': (0, pi),
            'xlabel': r'${\Delta}\phi_{H,t\bar{t}}$',
        },
        'deltaPhiTopTopbar': {
            'binning': {'n_or_arr': 64, 'lo': 0, 'hi': pi},
            'xlim': (0, pi),
            'xlabel': r'${\Delta}\phi_{t,\bar{t}}$',
        },
        'ttHbb_label': {
            'binning': {'n_or_arr': 50, 'lo': 0, 'hi': 1},
            'xlim': (0, 1),
            'xlabel': 'signal',
        },
        'weights_nominal': {
            'binning': {'n_or_arr': 50, 'lo': 0, 'hi': 2},
            'xlim': (0, 2),
            'xlabel': 'weights (nominal)',
        },
    },
    'variables2d': {
        'electron_etaSC_vs_electron_pt': {
            'electron_pt': {
                'binning': {'n_or_arr': 400, 'lo': 0, 'hi': 2000},
                'xlim': (0, 500),
                'xlabel': "Electron $p_{T}$ [GeV]",
            },
            'electron_etaSC': {
                'binning': {'n_or_arr': 10, 'lo': -2.5, 'hi': 2.5},
                'xlim': (-2.5, 2.5),
                'ylabel': "Electron Supercluster $\eta$",
            },
        },
        'electron_phi_vs_electron_pt': {
            'electron_pt': {
                'binning': {'n_or_arr': 400, 'lo': 0, 'hi': 2000},
                'xlim': (0, 500),
                'xlabel': "Electron $p_{T}$ [GeV]",
            },
            'electron_phi': {
                'binning': {'n_or_arr': 128, 'lo': -pi, 'hi': pi},
                'xlim': (-pi, pi),
                'ylabel': "$\phi_{e}$",
            },
        },
        'electron_etaSC_vs_electron_phi': {
            'electron_phi': {
                'binning': {'n_or_arr': 128, 'lo': -pi, 'hi': pi},
                'xlim': (-pi, pi),
                'xlabel': "$\phi_{e}$",
            },
            'electron_etaSC': {
                'binning': {'n_or_arr': 10, 'lo': -2.5, 'hi': 2.5},
                'xlim': (-2.5, 2.5),
                'ylabel': "Electron Supercluster $\eta$",
            },
        },
        'm_top_vs_met': {
            'met': {
                'binning': {'n_or_arr': 200, 'lo': 0, 'hi': 2000},
                'xlim': (0, 300),
                'xlabel': "$p_{T}^{MET}$ [GeV]",
            },
            'm_top': {
                'binning': {'n_or_arr': 200, 'lo': 0, 'hi': 2000},
                'ylim': (0, 500),
                'ylabel': "$m_{t}$ [GeV]",
            },
        },
    },
    'fill_opts': {
        'facecolor': "None",
        'edgecolor': ['#ff8000', '#0080ff'],
        'alpha': 1.0,
    },
    'error_opts': {
        #'label': 'Stat. Unc.',
        #'hatch': '///',
        'facecolor': 'none',
        'edgecolor': (0, 0, 0, 0.5),
        'linewidth': 0,
        #'elinewidth': 0
    },
}
