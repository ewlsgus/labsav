def msd(self, mode='single_frame', write="", start=0, end=0, exclude=[], window_size=10):
    r'''
        Returns the msd values for single frame or outputs the msd values
        for multiple frames to the csv file specified in <write>. For single
        frame values, specify the reference frame in <start> and the
        frame-to-be-analyzed in <end>. To analyze only specific particle
        type(s), specify the list of particle type(s) to be excluded in 
        <exclude>. If multiple frames are analyzed, the mode can be 
        specified as "fixed" or "moving" to calculate either the MSD with 
        respect to the <start> frame up to <end> or the moving average. For the moving 
        average, the window size can be specified with <window_size>.
    '''
    if mode=="single_frame":
        frame_ref=self.pipeline.gsd[start]
        frame_analyze=self.pipeline.gsd[end]
        distance_moved = self.distance(frame_ref, frame_analyze, frame_analyze.configuration.box[0:3])
    elif mode=="fixed":
        pass
    elif mode=="moving":
        pass
    else:
        raise Exception("Incorrect mode specification")
    return
    